import pandas as pd
from pathlib import Path
from sqlalchemy.engine import Engine

RAW_FILES = {
    "raw_orders": "olist_orders_dataset.csv",
    "raw_order_items": "olist_order_items_dataset.csv",
    "raw_customers": "olist_customers_dataset.csv",
    "raw_products": "olist_products_dataset.csv",
    "raw_sellers": "olist_sellers_dataset.csv",
    "raw_payments": "olist_order_payments_dataset.csv",
    "raw_reviews": "olist_order_reviews_dataset.csv",
    "raw_geolocation": "olist_geolocation_dataset.csv",
    "raw_category_translation": "product_category_name_translation.csv",
}

def load_csv_to_table(csv_path: Path, table_name: str, engine: Engine) -> int:
    """Load a single CSV into a Postgres table, unmodified. Returns row count loaded."""
    if not csv_path.exists():
        raise FileNotFoundError(f"Expected raw file not found: {csv_path}")
    df = pd.read_csv(csv_path)
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    return len(df)

def load_all_raw(raw_dir: Path, engine: Engine) -> dict:
    """Load every known raw file. Returns {table_name: row_count}."""
    results = {}
    for table_name, filename in RAW_FILES.items():
        count = load_csv_to_table(raw_dir / filename, table_name, engine)
        results[table_name] = count
    return results