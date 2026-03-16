from app.data.loader import load_transactions
from app.services.anomaly_detection import (
    detect_large_transactions,
    detect_duplicate_payments
)


def generate_anomaly_report():

    df = load_transactions()

    total_transactions = len(df)

    large_transactions = detect_large_transactions(df)
    duplicate_payments = detect_duplicate_payments(df)

    anomalies = []

    for tx in large_transactions:
        tx["anomaly_type"] = "large_transaction"
        anomalies.append(tx)

    for tx in duplicate_payments:
        tx["anomaly_type"] = "duplicate_payment"
        anomalies.append(tx)

    report = {
        "summary": {
            "transactions_analyzed": total_transactions,
            "anomalies_detected": len(anomalies),
            "large_transactions": len(large_transactions),
            "duplicate_payments": len(duplicate_payments),
        },
        "anomalies": anomalies
    }

    return report
