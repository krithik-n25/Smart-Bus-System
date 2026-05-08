from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from app.core.config import settings
from app.api.routes import auth

# Rate limiter setup
limiter = Limiter(key_func=get_remote_address)

app = FastAPI(
    title="Chalo API",
    description="Smart Bus Management System for Ahmedabad",
    version="1.0.0"
)

# Attach rate limiter to app
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# CORS — allows React frontend to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(auth.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {
        "app": "Chalo",
        "tagline": "Sahi bus, sahi samay, sahi jagya",
        "status": "running",
        "version": "1.0.0"
    }

@app.get("/health")
async def health():
    return {"status": "healthy", "supabase": "connected"}