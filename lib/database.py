# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembic import command
from alembic.config import Config

DATABASE_URL = "sqlite:///notes.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
db_session = Session()

def initialize_database(alembic_config):
    # Use Alembic to upgrade the database schema
    command.upgrade(alembic_config, "head")

if __name__ == "__main__":
    # Load Alembic configuration from the alembic.ini file
    alembic_config = Config("alembic.ini")
    
    # Call initialize_database with the Alembic configuration
    initialize_database(alembic_config)
