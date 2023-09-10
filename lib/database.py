from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base

def init_database(db_url='sqlite:///expense_tracker.db'):
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()
