# app/models/token.py



from sqlalchemy import Column, String, DateTime, ForeignKey
from datetime import datetime, timezone
import uuid

from app.db.base import Base

class Token(Base):
    __tablename__ = "tokens"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(ForeignKey("users.id"), nullable=False)

    type = Column(String, nullable=False)  # "verify_email" | "reset_password"
    expires_at = Column(DateTime(timezone=True), nullable=False)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
