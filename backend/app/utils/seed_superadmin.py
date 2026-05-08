"""
Run this ONCE to create the superadmin.
Never expose this as an API endpoint.
Run from terminal: python -m app.utils.seed_superadmin
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.config import supabase_admin
from app.core.security import hash_password

def create_superadmin():
    email = "admin@chalo.app"
    password = "Chalo@Admin2024!"

    # Check if already exists
    existing = supabase_admin.table("users").select("id").eq("email", email).execute()
    if existing.data:
        print("Superadmin already exists")
        return

    hashed = hash_password(password)

    result = supabase_admin.table("users").insert({
        "email": email,
        "hashed_password": hashed,
        "role": "admin",
        "full_name": "Chalo Super Admin",
        "is_active": True,
        "language_preference": "en"
    }).execute()

    print("Superadmin created successfully")
    print(f"Email: {email}")
    print(f"Password: {password}")
    print("CHANGE THIS PASSWORD IMMEDIATELY AFTER FIRST LOGIN")

if __name__ == "__main__":
    create_superadmin()