import pandas as pd
from pathlib import Path

# Automatically get project root (the folder that contains "src")
PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

def load_olist_raw():
    """Load all raw Olist CSVs into a dictionary of DataFrames."""

    files = {
        "orders": "olist_orders_dataset.csv",
        "order_items": "olist_order_items_dataset.csv",
        "order_payments": "olist_order_payments_dataset.csv",
        "order_reviews": "olist_order_reviews_dataset.csv",
        "products": "olist_products_dataset.csv",
        "sellers": "olist_sellers_dataset.csv",
        "customers": "olist_customers_dataset.csv",
    }

    df = {}
    for key, filename in files.items():
        file_path = RAW_DATA_DIR / filename
        if not file_path.exists():
            raise FileNotFoundError(f"Missing file: {file_path}")

        df[key] = pd.read_csv(file_path)
        print(f"Loaded: {key} — {df[key].shape}")

    return df
