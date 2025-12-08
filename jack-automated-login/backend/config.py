import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    if DATABASE_URL is None:
        raise Exception("DATABASE_URL is not set in .env")
    return psycopg2.connect(DATABASE_URL)
