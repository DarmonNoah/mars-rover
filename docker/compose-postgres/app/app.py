import os
import time
import psycopg2

host = os.getenv("DB_HOST", "localhost")
print(f"🔍 Tentative de connexion à PostgreSQL sur {host}...")

while True:
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="example",
            host=host,
            port=5432
        )
        print("✅ Connexion réussie à PostgreSQL !")
        break
    except Exception as e:
        print(f"⏳ En attente de PostgreSQL... ({e})")
        time.sleep(2)
