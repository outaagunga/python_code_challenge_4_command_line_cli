# env.py
from alembic import context
from sqlalchemy import create_engine
from lib.config import DATABASE_URL

# Load the models to ensure they are available for Alembic
from lib.models import *

# Define the metadata for the database
target_metadata = Base.metadata

# ...

def run_migrations_online():
    # ...

    # Create the initial database if it doesn't exist
    engine = create_engine(DATABASE_URL)
    conn = engine.connect()
    conn.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE_URL.split('/')[-1]}")
    conn.close()

    # ...
