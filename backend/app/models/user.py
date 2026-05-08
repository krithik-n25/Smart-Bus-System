from pydantic import BaseModel, EmailStr, validator
from typing import Optional
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    admin = "admin"
    driver = "driver"
    passenger = "passenger"

class UserRegister(BaseModel):
    """What passenger sends to register themselves."""
    email: EmailStr
    password: str
    full_name: str
    phone: Optional[str] = None
    language_preference: str = "en"

class UserLogin(BaseModel):
    """What any user sends to login."""
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    """What we send back — never includes password."""
    id: str
    email: str
    role: UserRole
    full_name: Optional[str]
    phone: Optional[str]
    language_preference: str
    is_active: bool
    created_at: datetime

class TokenResponse(BaseModel):
    """What we send back after successful login."""
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    role: UserRole
    user: UserResponse

class TokenRefreshRequest(BaseModel):
    """What frontend sends to get new access token."""
    refresh_token: str

class CreateDriverRequest(BaseModel):
    """Only admin can use this to create driver accounts."""
    email: EmailStr
    full_name: str
    phone: Optional[str] = None

class ChangePasswordRequest(BaseModel):
    current_password: str
    new_password: str