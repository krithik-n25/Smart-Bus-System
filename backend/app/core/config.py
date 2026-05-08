from pydantic_settings import BaseSettings, SettingsConfigDict
from supabase import create_client, Client
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "Chalo"
    
    # Supabase Connection
    # These will be read from your .env file
    SUPABASE_URL: str
    SUPABASE_KEY: str  # The "anon" public key
    SUPABASE_SERVICE_ROLE_KEY: str  # The "service_role" secret key
    
    # JWT Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore"
    )

# Create settings instance
settings = Settings()

# Initialize Supabase Admin Client
# This is used for backend operations that need to bypass RLS or manage users
supabase_admin: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_SERVICE_ROLE_KEY)
