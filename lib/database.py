from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembic import command

DATABASE_URL = "sqlite:///notes.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
db_session = Session()

def initialize_database():
    # Remove this line that automatically creates tables
    # Base.metadata.create_all(engine)

    # Use Alembic to upgrade the database schema
    command.upgrade(engine, "head")
