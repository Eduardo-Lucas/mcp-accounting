import time
import psycopg2
import os

DB_URL = os.getenv("DATABASE_URL")

print("Waiting for database...")

while True:
    try:
        conn = psycopg2.connect(DB_URL)
        conn.close()
        print("Database is ready!")
        break
    except psycopg2.OperationalError:
        print("Database not ready, retrying...")
        time.sleep(2)
