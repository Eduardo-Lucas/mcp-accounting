# app/services/token_service.py

from datetime import datetime, timedelta, timezone
from app.models.token import Token

TOKEN_EXPIRATION_MINUTES = 60

def create_token(db, user_id: str, token_type: str):
    token = Token(
        user_id=user_id,
        type=token_type,
        expires_at=datetime.now(timezone.utc) + timedelta(minutes=TOKEN_EXPIRATION_MINUTES)
    )
    db.add(token)
    db.commit()
    db.refresh(token)
    return token


def validate_token(db, token_id: str, token_type: str):
    token = db.query(Token).filter_by(id=token_id, type=token_type).first()

    if not token:
        return None

    if token.expires_at < datetime.now(timezone.utc):
        return None

    return token
