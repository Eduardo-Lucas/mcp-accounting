from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from pathlib import Path
import pandas as pd
from sqlalchemy.orm import Session
from datetime import timedelta

from app.db.session import get_db
from app.models.transaction import Transaction
from app.models.user import User
from app.core.security import hash_password
from app.services.auth_service import authenticate_user
from app.core.jwt import create_access_token
from app.schemas.auth import LoginSchema, TokenResponse

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
    user = authenticate_user(db, data.email, data.password)

    access_token = create_access_token(
        data={"sub": str(user.id)},
        expires_delta=timedelta(minutes=30)
    )

    return {"access_token": access_token}


@router.post("/auth/register")
def register(data: LoginSchema, db: Session = Depends(get_db)):
    user = User(
        email=data.email,
        hashed_password=hash_password(data.password)
    )
    db.add(user)
    db.commit()

    return {"message": "User created"}
