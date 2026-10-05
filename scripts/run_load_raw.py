from pathlib import Path
from src.warehouse.config import get_engine
from load_raw import load_all_raw


if __name__ == "__main__":
    engine = get_engine()
    raw_dir = Path("data/raw")
    results = load_all_raw(raw_dir, engine)
    for table, count in results.items():
        print(f"{table}: {count:,} rows loaded")