# app/core/jwt.py
from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "your-secret"  # move to env
ALGORITHM = "HS256"

def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    to_encode["exp"] = datetime.utcnow() + expires_delta
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
