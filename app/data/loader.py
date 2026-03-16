import pandas as pd
from app.core.config import DATA_FILE


def load_transactions():
    if not DATA_FILE.exists():
        return pd.DataFrame()

    df = pd.read_csv(DATA_FILE)
    df.columns = [c.lower() for c in df.columns]

    return df
