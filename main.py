import click
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

# Database setup
engine = create_engine('sqlite:///expense_tracker.db')
Session = sessionmaker(bind=engine)
session = Session()

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

# Helper functions
def init_database():
    Base.metadata.create_all(engine)

def print_help():
    click.echo("Available commands:")
    click.echo("  add - Add a user or expense")
    click.echo("  list - List users or expenses")
    click.echo("  view - View user details or expense details")
    click.echo("  edit - Edit user or expense")
    click.echo("  delete - Delete user or expense")
    click.echo("  sort - Sort expenses by category")
    click.echo("  exit - Exit the program")

@click.command()
def cli():
    click.echo("Welcome to the Expense Tracker!")
    init_database()  # Initialize the database
    while True:
        user_input = click.prompt("Enter a command (type 'help' for available commands):")
        if user_input == 'help':
            print_help()
        elif user_input == 'add':
            add()
        elif user_input == 'list':
            list_entities()
        elif user_input == 'view':
            view()
        elif user_input == 'edit':
            edit()
        elif user_input == 'delete':
            delete()
        elif user_input == 'sort':
            sort()
        elif user_input == 'exit':
            exit_program()
            break
        else:
            click.echo("Invalid command. Type 'help' for available commands.")

def add():
    entity = click.prompt("Select 'user' or 'expense'", type=click.Choice(["user", "expense"]))
    if entity == "user":
        username = click.prompt("Enter username")
        try:
            user = User(username=username)
            session.add(user)
            session.commit()
            click.echo(f"User {username} added!")
        except IntegrityError:
            session.rollback()
            click.echo(f"Error: Username {username} already exists.")
    elif entity == "expense":
        name = click.prompt("Enter expense name")
        amount = click.prompt("Enter expense amount", type=float)
        category_name = click.prompt("Enter expense category")
        category = session.query(Category).filter_by(name=category_name).first()
        if category is None:
            click.echo("Error: Category does not exist.")
            return
        try:
            expense = Expense(name=name, amount=amount, category=category)
            session.add(expense)
            session.commit()
            click.echo(f"Expense added: {expense.name}, ${expense.amount}, Category: {expense.category.name}")
        except IntegrityError:
            session.rollback()
            click.echo("Error: Invalid input or category does not exist.")

def list_entities():
    entity = click.prompt("Select 'user' or 'expense'", type=click.Choice(["user", "expense"]))
    if entity == "user":
        users = session.query(User).all()
        click.echo("Users:")
        for user in users:
            click.echo(f"{user.id}: {user.username}")
    elif entity == "expense":
        expenses = session.query(Expense).all()
        click.echo("Expenses:")
        for expense in expenses:
            click.echo(f"{expense.id}: {expense.name}, ${expense.amount}, Category: {expense.category.name}")

def view():
    entity = click.prompt("Select 'user' or 'expense'", type=click.Choice(["user", "expense"]))
    try:
        entity_id = click.prompt("Enter the ID of the entity to view", type=int)
        if entity == "user":
            user = session.query(User).get(entity_id)
            if user:
                click.echo(f"User details: {user.id}: {user.username}")
            else:
                click.echo("User not found.")
        elif entity == "expense":
            expense = session.query(Expense).get(entity_id)
            if expense:
                click.echo(f"Expense details: {expense.id}: {expense.name}, ${expense.amount}, Category: {expense.category.name}")
            else:
                click.echo("Expense not found.")
    except SQLAlchemyError:
        click.echo("Error: Invalid input or entity does not exist.")

def edit():
    entity = click.prompt("Select 'user' or 'expense'", type=click.Choice(["user", "expense"]))
    try:
        entity_id = click.prompt("Enter the ID of the entity to edit", type=int)
        if entity == "user":
            user = session.query(User).get(entity_id)
            if user:
                new_username = click.prompt("Enter new username", default=user.username)
                user.username = new_username
                session.commit()
                click.echo(f"User {user.id} updated!")
            else:
                click.echo("User not found.")
        elif entity == "expense":
            expense = session.query(Expense).get(entity_id)
            if expense:
                new_name = click.prompt("Enter new expense name", default=expense.name)
                new_amount = click.prompt("Enter new expense amount", default=expense.amount, type=float)
                new_category = click.prompt("Enter new expense category", default=expense.category.name)
                category = session.query(Category).filter_by(name=new_category).first()
                if category is None:
                    click.echo("Error: Category does not exist.")
                    return
                expense.name = new_name
                expense.amount = new_amount
                expense.category = category
                session.commit()
                click.echo(f"Expense {expense.id} updated!")
            else:
                click.echo("Expense not found.")
    except SQLAlchemyError:
        session.rollback()
        click.echo("Error: Invalid input or entity does not exist.")

def delete():
    entity = click.prompt("Select 'user' or 'expense'", type=click.Choice(["user", "expense"]))
    try:
        entity_id = click.prompt("Enter the ID of the entity to delete", type=int)
        if entity == "user":
            user = session.query(User).get(entity_id)
            if user:
                session.delete(user)
                session.commit()
                click.echo(f"User {user.id} deleted!")
            else:
                click.echo("User not found.")
        elif entity == "expense":
            expense = session.query(Expense).get(entity_id)
            if expense:
                session.delete(expense)
                session.commit()
                click.echo(f"Expense {expense.id} deleted!")
            else:
                click.echo("Expense not found.")
    except SQLAlchemyError:
        session.rollback()
        click.echo("Error: Invalid input or entity does not exist.")

def sort():
    try:
        expenses = session.query(Expense).order_by(Expense.category_id).all()
        click.echo("Expenses (sorted by category):")
        for expense in expenses:
            click.echo(f"{expense.id}: {expense.name}, ${expense.amount}, Category: {expense.category.name}")
    except SQLAlchemyError:
        click.echo("Error: Unable to retrieve and sort expenses.")

def exit_program():
    click.echo("Exiting the program.")
    session.close()

if __name__ == "__main__":
    cli()
