from app.data.loader import load_transactions
from app.services.anomaly_detection import (
    detect_large_transactions,
    detect_duplicate_payments
)

from app.services.explanation_service import explain_anomalies


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
        "anomalies": explain_anomalies(anomalies)
    }

    return report


from app.data.loader import load_transactions
from app.services.anomaly_detection import (
    detect_large_transactions,
    detect_duplicate_payments
)
from app.services.explanation_service import explain_anomalies


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

    return {
        "summary": {
            "transactions_analyzed": total_transactions,
            "anomalies_detected": len(anomalies),
        },
        "anomalies": anomalies
    }


def generate_explained_report():

    report = generate_anomaly_report()

    anomalies = report["anomalies"]

    explained = explain_anomalies(anomalies)

    report["anomalies"] = explained

    return report

