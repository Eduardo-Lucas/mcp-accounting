from openai import OpenAI
from app.core.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def explain_anomaly(anomaly: dict):

    prompt = f"""
You are an accounting auditor.

Explain briefly (1–2 sentences) why this transaction might be suspicious.

Transaction:
Vendor: {anomaly.get("vendor")}
Amount: {anomaly.get("amount")}
Description: {anomaly.get("description")}
Reason flagged: {anomaly.get("reason")}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a financial audit assistant."},
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content


def explain_anomalies(anomalies):

    results = []

    for anomaly in anomalies:

        explanation = explain_anomaly(anomaly)

        anomaly["ai_explanation"] = explanation

        results.append(anomaly)

    return results
