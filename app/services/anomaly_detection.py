import pandas as pd


def detect_large_transactions(df):

    if df.empty:
        return []

    # 95th percentile threshold
    threshold = round(df["amount"].quantile(0.95), 2)

    anomalies = df[df["amount"] > threshold]

    results = []

    for _, row in anomalies.iterrows():
        results.append(
            {
                "date": row["date"],
                "vendor": row["vendor"],
                "amount": f"{row['amount']:.2f}",
                "description": row["description"],
                "threshold": f"{threshold:.2f}",
                "reason": "Transaction above 95th percentile of amounts",
            }
        )

    return results


def detect_duplicate_payments(df: pd.DataFrame):

    duplicates = df[df.duplicated(
        subset=["vendor", "amount"], keep=False
    )]

    duplicates = duplicates.copy()
    duplicates["amount"] = duplicates["amount"].apply(lambda x: f"{x:.2f}")

    return duplicates.to_dict(orient="records")
