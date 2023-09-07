# models.py
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

# Define your SQLAlchemy engine and session here
DATABASE_URL = "sqlite:///notes.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
db_session = Session()

note_tag_association = Table(
    "note_tag_association",
    Base.metadata,
    Column("note_id", Integer, ForeignKey("notes.id")),
    Column("tag_id", Integer, ForeignKey("tags.id")),
)

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    notes = relationship("Note", back_populates="category")

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    notes = relationship("Note", secondary=note_tag_association)

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="notes")
    tags = relationship("Tag", secondary=note_tag_association)
