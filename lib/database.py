# database.py
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembic.config import Config
from alembic import command
from sqlalchemy import exc as sqlalchemy_exc

from lib.config import DATABASE_URL

def initialize_database():
    print(f"Database URL: {DATABASE_URL}")
    try:
        engine = create_engine(DATABASE_URL)
    except sqlalchemy_exc.OperationalError as e:
        print(f"Error connecting to the database: {str(e)}")
        sys.exit(1)

    Session = sessionmaker(bind=engine)
    db_session = Session()

    alembic_config = Config("alembic.ini")
    command.upgrade(alembic_config, "head")

    return db_session
