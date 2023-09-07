#  env.py

from alembic import context
from sqlalchemy import create_engine

# ...

def run_migrations_online():
    # ...

    # Create the initial database if it doesn't exist
    from lib.config import DATABASE_URL

    engine = create_engine(DATABASE_URL)
    conn = engine.connect()
    conn.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE_URL.split('/')[-1]}")
    conn.close()

    # ...
