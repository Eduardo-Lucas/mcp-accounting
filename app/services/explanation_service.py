from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def explain_anomaly(anomaly: dict):

    prompt = f"""
You are an accounting auditor.

Explain why the following transaction may be suspicious.

Transaction:
Vendor: {anomaly.get("vendor")}
Amount: {anomaly.get("amount")}
Description: {anomaly.get("description")}
Reason flagged: {anomaly.get("reason")}

Provide a short explanation understandable by an accountant.
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a financial audit assistant."},
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content
