from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from pathlib import Path
import pandas as pd
from sqlalchemy.orm import Session
from datetime import timedelta

from app.core.jwt import create_access_token
from app.core.security import verify_password
from app.db.session import get_db
from app.models.transaction import Transaction
from app.models.user import User
from app.core.security import hash_password
from app.services.auth_service import authenticate_user
from app.services.token_service import create_token, validate_token
from app.services.email_service import send_email
from app.config import FRONTEND_URL

from app.schemas.auth import (
    LoginSchema, 
    TokenResponse, 
    UserCreate, 
    ForgotPasswordRequest, 
    ResetPasswordRequest
)


from app.mcp.tools import (
    get_transactions,
    detect_large_expenses,
    find_duplicate_payments
)

from app.services.report_services import (
    generate_anomaly_report,
    generate_explained_report
)

router = APIRouter()

DATA_DIR = Path("data")


# -------------------------
# TOOLS
# -------------------------

@router.get("/tools")
def list_tools():
    return {
        "tools": [
            "get_transactions",
            "detect_large_expenses",
            "find_duplicate_payments"
        ]
    }


@router.post("/tools/get_transactions")
def api_transactions():
    return {"results": get_transactions()}


@router.post("/tools/detect_large_expenses")
def api_large_expenses():
    return {"results": detect_large_expenses()}


@router.post("/tools/find_duplicate_payments")
def api_duplicates():
    return {"results": find_duplicate_payments()}


# -------------------------
# INGESTION
# -------------------------

@router.post("/upload-transactions")
def upload_transactions(file: UploadFile = File(...), db: Session = Depends(get_db)):
    df = pd.read_csv(file.file)

    for _, row in df.iterrows():
        tx = Transaction(
            date=row["date"],
            description=row["description"],
            vendor=row["vendor"],
            amount=row["amount"]
        )
        db.add(tx)

    db.commit()

    return {
        "message": "transactions ingested",
        "rows": len(df)
    }


# -------------------------
# REPORTS
# -------------------------

@router.post("/report/anomalies")
def anomaly_report():
    return generate_anomaly_report()


@router.post("/report/anomalies/explain")
def anomaly_report_with_explanations():
    return generate_explained_report()


# -------------------------
# AUTH
# -------------------------

@router.post("/auth/login", response_model=TokenResponse)
def login(data: LoginSchema, db: Session = Depends(get_db)):

    user = db.query(User).filter_by(email=data.email).first()

    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    if not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    if not user.is_verified:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    access_token = create_access_token({"sub": user.email})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.post("/auth/register")
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    # 🔍 DEBUG START
    print("user_in:", user_in)
    print("password:", user_in.password)
    print("type:", type(user_in.password))
    print("length:", len(user_in.password))
    # 🔍 DEBUG END
    existing = db.query(User).filter_by(email=user_in.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = User(
        email=user_in.email,
        hashed_password=hash_password(user_in.password),
        is_active=False,
        is_verified=False
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    token = create_token(db, user.id, "verify_email")

    verification_link = f"{FRONTEND_URL}/verify-email?token={token.id}"

    send_email(
        to=user.email,
        subject="Verify your account",
        body=f"Click here: {verification_link}"
    )

    return {"message": "User created. Check your email."}


@router.get("/verify-email")
def verify_email(token: str, db: Session = Depends(get_db)):
    token_obj = validate_token(db, token, "verify_email")

    if not token_obj:
        raise HTTPException(status_code=400, detail="Invalid or expired token")

    user = db.get(User, token_obj.user_id)
    user.is_active = True
    user.is_verified = True

    db.delete(token_obj)

    db.commit()

    return {"message": "Email verified successfully"}


@router.post("/forgot-password")
def forgot_password(email: str, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(email=email).first()

    if not user:
        # Prevent enumeration
        return {"message": "If the email exists, a reset link was sent"}

    token = create_token(db, user.id, "reset_password")

    reset_link = f"{FRONTEND_URL}/reset-password?token={token.id}"

    send_email(
        to=user.email,
        subject="Reset your password",
        body=f"Click here: {reset_link}"
    )

    return {"message": "If the email exists, a reset link was sent"}



@router.post("/reset-password")
def reset_password(data: ResetPasswordRequest, db: Session = Depends(get_db)):
    token_obj = validate_token(db, data.token, "reset_password")

    if not token_obj:
        raise HTTPException(status_code=400, detail="Invalid or expired token")

    user = db.query(User).get(token_obj.user_id)
    user.password_hash = hash_password(data.new_password)

    db.commit()

    return {"message": "Password updated successfully"}
