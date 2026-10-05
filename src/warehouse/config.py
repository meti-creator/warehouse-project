import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

def get_engine():
    user = os.environ["DB_USER"]
    password = os.environ["DB_PASSWORD"]
    host = os.environ["DB_HOST"]
    port = os.environ["DB_PORT"]
    dbname = os.environ["DB_NAME"]
    url = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
    return create_engine(url)