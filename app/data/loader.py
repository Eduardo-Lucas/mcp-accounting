from app.db.session import SessionLocal
from app.models.transaction import Transaction
import pandas as pd



def load_transactions():
    db = SessionLocal()

    rows = db.query(Transaction).all()

    db.close()

    data = [
        {
            "date": r.date,
            "description": r.description,
            "vendor": r.vendor,
            "amount": r.amount
        }
        for r in rows
    ]

    return pd.DataFrame(data)
