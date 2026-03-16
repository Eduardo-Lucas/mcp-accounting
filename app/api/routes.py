from fastapi import APIRouter
from app.mcp.tools import (
    get_transactions,
    detect_large_expenses,
    find_duplicate_payments
)

router = APIRouter()


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
