from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembic import command

DATABASE_URL = "sqlite:///notes.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
db_session = Session()

def initialize_database():
    command.upgrade(engine, "head")
