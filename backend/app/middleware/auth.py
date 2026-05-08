from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.security import decode_token
from app.core.config import supabase_admin

# This tells FastAPI to look for "Bearer <token>" in the Authorization header
security = HTTPBearer()

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """
    Dependency that validates token and returns current user.
    Use this on any endpoint that requires login.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired token",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token = credentials.credentials
    payload = decode_token(token)

    if payload is None:
        raise credentials_exception

    # Make sure this is an access token, not a refresh token
    if payload.get("type") != "access":
        raise credentials_exception

    user_id = payload.get("sub")
    if user_id is None:
        raise credentials_exception

    # Fetch user from database to confirm they still exist and are active
    try:
        result = supabase_admin.table("users").select("*").eq("id", user_id).single().execute()
        user = result.data
    except Exception:
        raise credentials_exception

    if not user:
        raise credentials_exception

    if not user.get("is_active"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account is deactivated"
        )

    return user

async def require_admin(current_user: dict = Depends(get_current_user)):
    """Only admins can access this endpoint."""
    if current_user["role"] != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return current_user

async def require_driver(current_user: dict = Depends(get_current_user)):
    """Only drivers can access this endpoint."""
    if current_user["role"] != "driver":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Driver access required"
        )
    return current_user

async def require_admin_or_driver(current_user: dict = Depends(get_current_user)):
    """Both admins and drivers can access this endpoint."""
    if current_user["role"] not in ["admin", "driver"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin or Driver access required"
        )
    return current_user