# lib/models.py

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    expenses = relationship('Expense', back_populates='user')

class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='expenses')
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='expenses')

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    expenses = relationship('Expense', back_populates='category')
