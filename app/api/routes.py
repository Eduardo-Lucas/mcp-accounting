from fastapi import APIRouter, UploadFile, File
from pathlib import Path
import shutil

from app.mcp.tools import (
    get_transactions,
    detect_large_expenses,
    find_duplicate_payments
)
from app.services.report_services import generate_anomaly_report

router = APIRouter()

DATA_DIR = Path("data")


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


@router.post("/upload-transactions")
def upload_transactions(file: UploadFile = File(...)):

    DATA_DIR.mkdir(exist_ok=True)

    file_path = DATA_DIR / "transactions.csv"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "file uploaded successfully",
        "filename": file.filename
    }


@router.post("/report/anomalies")
def anomaly_report():

    return generate_anomaly_report()
