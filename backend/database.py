import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

database_url = os.environ.get("DATABASE_URL")

def db_connect():
    try:
        conn = psycopg2.connect(database_url)
        print("database connected")
    except Exception as e:
        print(f"database hasnt connected, error: {e}")