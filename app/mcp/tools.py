from app.data.loader import load_transactions
from app.services.anomaly_detection import (
    detect_large_transactions,
    detect_duplicate_payments
)


def get_transactions():

    df = load_transactions()
    return df.to_dict(orient="records")


def detect_large_expenses():

    df = load_transactions()
    return detect_large_transactions(df)


def find_duplicate_payments():

    df = load_transactions()
    return detect_duplicate_payments(df)
