import os
import psycopg2
import psycopg2.extras

DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    DATABASE_URL = os.getenv("DATABASE_URL")
    if not DATABASE_URL:
        raise Exception("DATABASE_URL is not set in .env")

    return psycopg2.connect(
        DATABASE_URL,
        cursor_factory=psycopg2.extras.RealDictCursor
    )
