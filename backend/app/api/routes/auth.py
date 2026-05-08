from fastapi import APIRouter, HTTPException, status, Depends, Request
from app.models.user import (
    UserRegister, UserLogin, TokenResponse,
    TokenRefreshRequest, CreateDriverRequest,
    ChangePasswordRequest, UserResponse
)
from app.core.security import (
    hash_password, verify_password,
    validate_password_strength,
    create_access_token, create_refresh_token,
    decode_token
)
from app.core.config import supabase_admin
from app.middleware.auth import get_current_user, require_admin
from app.utils.audit import log_audit
import secrets
import string

router = APIRouter(prefix="/auth", tags=["Authentication"])

# ─────────────────────────────────────────
# PASSENGER SELF REGISTRATION
# ─────────────────────────────────────────
@router.post("/register", response_model=TokenResponse)
async def register(data: UserRegister, request: Request):
    """
    Passengers register themselves.
    Drivers and admins cannot use this endpoint.
    """
    # 1. Validate password strength
    is_valid, message = validate_password_strength(data.password)
    if not is_valid:
        raise HTTPException(status_code=400, detail=message)

    # 2. Check if email already exists
    existing = supabase_admin.table("users").select("id").eq("email", data.email).execute()
    if existing.data:
        raise HTTPException(status_code=400, detail="Email already registered")

    # 3. Hash password — never store plain text
    hashed = hash_password(data.password)

    # 4. Create user in database
    new_user = supabase_admin.table("users").insert({
        "email": data.email,
        "hashed_password": hashed,
        "role": "passenger",
        "full_name": data.full_name,
        "phone": data.phone,
        "language_preference": data.language_preference,
        "is_active": True
    }).execute()

    user = new_user.data[0]

    # 5. Generate tokens
    access_token = create_access_token({"sub": user["id"], "role": user["role"]})
    refresh_token = create_refresh_token({"sub": user["id"], "role": user["role"]})

    # 6. Log the registration
    await log_audit(user["id"], "REGISTER", "users", user["id"], None, {"email": data.email})

    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token,
        role=user["role"],
        user=UserResponse(**user)
    )

# ─────────────────────────────────────────
# LOGIN — ALL ROLES
# ─────────────────────────────────────────

from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@router.post("/login", response_model=TokenResponse)
@limiter.limit("5/minute")  # Max 5 login attempts per minute per IP
async def login(data: UserLogin, request: Request):
    """
    Login for all roles.
    System detects role automatically from database.
    """
    # 1. Find user by email
    result = supabase_admin.table("users").select("*").eq("email", data.email).execute()

    if not result.data:
        # Don't say "user not found" — say "invalid credentials"
        # This prevents attackers from knowing which emails exist
        raise HTTPException(status_code=401, detail="Invalid credentials")

    user = result.data[0]

    # 2. Check account is active
    if not user["is_active"]:
        raise HTTPException(status_code=403, detail="Account deactivated. Contact admin.")

    # 3. Verify password
    if not verify_password(data.password, user["hashed_password"]):
        # Log failed attempt
        await log_audit(None, "LOGIN_FAILED", "users", user["id"], None, {"email": data.email})
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # 4. Update last login timestamp
    supabase_admin.table("users").update(
        {"last_login": "now()"}
    ).eq("id", user["id"]).execute()

    # 5. Create tokens with role embedded inside
    token_data = {"sub": user["id"], "role": user["role"]}
    access_token = create_access_token(token_data)
    refresh_token = create_refresh_token(token_data)

    # 6. Log successful login
    await log_audit(user["id"], "LOGIN_SUCCESS", "users", user["id"], None, None)

    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token,
        role=user["role"],
        user=UserResponse(**user)
    )

# ─────────────────────────────────────────
# REFRESH TOKEN
# ─────────────────────────────────────────
@router.post("/refresh")
async def refresh_token(data: TokenRefreshRequest):
    """
    Get a new access token using refresh token.
    Called automatically by frontend when access token expires.
    """
    payload = decode_token(data.refresh_token)

    if payload is None or payload.get("type") != "refresh":
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    user_id = payload.get("sub")

    # Confirm user still exists and is active
    result = supabase_admin.table("users").select("*").eq("id", user_id).single().execute()
    user = result.data

    if not user or not user["is_active"]:
        raise HTTPException(status_code=401, detail="User no longer active")

    # Issue new access token
    new_access_token = create_access_token({"sub": user["id"], "role": user["role"]})

    return {"access_token": new_access_token, "token_type": "bearer"}

# ─────────────────────────────────────────
# LOGOUT
# ─────────────────────────────────────────
@router.post("/logout")
async def logout(current_user: dict = Depends(get_current_user)):
    """
    Logout current user.
    In a full system, we'd blacklist the token here.
    For now, client deletes the token.
    """
    await log_audit(current_user["id"], "LOGOUT", "users", current_user["id"], None, None)
    return {"message": "Logged out successfully"}

# ─────────────────────────────────────────
# GET CURRENT USER
# ─────────────────────────────────────────
@router.get("/me", response_model=UserResponse)
async def get_me(current_user: dict = Depends(get_current_user)):
    """Returns the currently logged in user's profile."""
    return UserResponse(**current_user)

# ─────────────────────────────────────────
# ADMIN CREATES DRIVER ACCOUNT
# ─────────────────────────────────────────
@router.post("/create-driver")
async def create_driver(
    data: CreateDriverRequest,
    admin: dict = Depends(require_admin)
):
    """
    Only admins can create driver accounts.
    Driver receives a temporary password.
    They must change it on first login.
    """
    # Check email doesn't exist
    existing = supabase_admin.table("users").select("id").eq("email", data.email).execute()
    if existing.data:
        raise HTTPException(status_code=400, detail="Email already exists")

    # Generate temporary password
    alphabet = string.ascii_letters + string.digits + "!@#$"
    temp_password = "".join(secrets.choice(alphabet) for _ in range(12))

    hashed = hash_password(temp_password)

    new_driver = supabase_admin.table("users").insert({
        "email": data.email,
        "hashed_password": hashed,
        "role": "driver",
        "full_name": data.full_name,
        "phone": data.phone,
        "language_preference": "gu",
        "is_active": True
    }).execute()

    driver = new_driver.data[0]

    await log_audit(
        admin["id"], "CREATE_DRIVER",
        "users", driver["id"],
        None, {"email": data.email, "created_by": admin["email"]}
    )

    # In production, email the temp password
    # For now, return it in response (only for development)
    return {
        "message": "Driver account created",
        "driver_id": driver["id"],
        "temp_password": temp_password,
        "note": "Share this password with the driver securely"
    }

# ─────────────────────────────────────────
# CHANGE PASSWORD
# ─────────────────────────────────────────
@router.post("/change-password")
async def change_password(
    data: ChangePasswordRequest,
    current_user: dict = Depends(get_current_user)
):
    """Any logged in user can change their own password."""
    # Verify current password
    if not verify_password(data.current_password, current_user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Current password is incorrect")

    # Validate new password strength
    is_valid, message = validate_password_strength(data.new_password)
    if not is_valid:
        raise HTTPException(status_code=400, detail=message)

    # Update password
    new_hash = hash_password(data.new_password)
    supabase_admin.table("users").update(
        {"hashed_password": new_hash}
    ).eq("id", current_user["id"]).execute()

    await log_audit(
        current_user["id"], "PASSWORD_CHANGE",
        "users", current_user["id"], None, None
    )

    return {"message": "Password changed successfully"}