Project Idea: Task Manager CLI

Project Description:
I will create a Command Line Interface (CLI) Task Manager application that allows me to manage my tasks. This project will help me learn and practice the concepts of database modeling with SQLAlchemy, working with CLI interfaces, and implementing a basic algorithm

Key Features:

Task Management: Users should be able to add, view, update, and delete tasks.

Task Categories: Tasks can belong to different categories (e.g., work, personal, shopping).

Due Dates: Each task can have an optional due date.

Priority: Allow users to assign a priority level to each task (e.g., high, medium, low).

CLI Interface: Implement a user-friendly CLI interface that allows users to interact with the task manager using commands and options.

Database: Use SQLAlchemy ORM to create a database schema with at least three related tables (e.g., Users, Tasks, Categories).

Algorithm: Implement a simple algorithm to sort tasks based on priority or due date.

Best Practices: Follow best practices in CLI design, code organization, and documentation.

Project Steps:

Plan the database schema, considering the tables needed for users, tasks, and categories, and define their relationships.

Set up a virtual environment using Pipenv.

Create Python classes for the database models (Users, Tasks, Categories) using SQLAlchemy ORM.

Build the CLI interface using a library like Click or Fire, allowing me to perform CRUD (Create, Read, Update, Delete) operations on tasks.

Implement the algorithm to sort tasks based on priority or due date.

Test the CLI application thoroughly to ensure it works as expected.

Organize the code into separate modules for database models, CLI commands, and utilities.

Document the code using comments and docstrings.

JUST FOR MY CONSUMPTION (Not yours please)

Step 3: Plan Your Database Schema
Before you write any code, plan your database schema. This means deciding what tables you need, their relationships, and the data they will store. This planning is essential because you'll be using SQLAlchemy ORM to create and modify the database.
...........................

Step 5: Define Your Database Models
Create Python classes to define your database models. These classes will represent tables in your database. Use SQLAlchemy ORM to define relationships between these tables (one-to-one, one-to-many, many-to-many).

Step 6: Create Your CLI Application
Create a separate module for your CLI application. You'll use libraries like Click or Fire to help with CLI functionality.

Define commands and options in your CLI application. Think about how users will interact with your program through the command line.

Step 7: Implement an Algorithm
Choose one or more algorithms from your Data Structures and Algorithms learning and implement them within your CLI application. Ensure they solve a real-world problem related to your project.

Step 8: Package Structure and Best Practices
Organize your project into a proper package structure. Place related code in separate modules.

Ensure you're using lists, dictionaries, and tuples where appropriate in your code.

Step 9: Testing and Debugging
Test your CLI application thoroughly to ensure it works as expected. Fix any bugs or issues that you encounter.

Step 10: Documentation
Document your code using comments and docstrings to explain how it works.

STEP-BY-STEP GUIDE TO planning your database schema:

Identify Data Entities:
Start by identifying the main data entities or objects in your project. In this case, you have:

Users
Tasks
Categories

Define Relationships:
Determine how these data entities are related to each other.

Consider the following relationships:

A user can have multiple tasks (one-to-many relationship).
Each task can belong to one category, but a category can have multiple tasks (one-to-many relationship between Tasks and Categories).

Design Tables:
For each data entity, design a table that represents it. Here's a rough outline of what the tables might look like:

Users Table:

Columns:
User ID (Primary Key)
Username
Password (hashed and salted for security)

Tasks Table:

Columns:
Task ID (Primary Key)
User ID (Foreign Key to Users)
Task Name
Description
Due Date (Nullable)
Priority (e.g., high, medium, low)
Category ID (Foreign Key to Categories)

Categories Table:

Columns:
Category ID (Primary Key)
Category Name
Primary Keys and Foreign Keys:

User ID in the Users table should be the primary key.
Task ID in the Tasks table and Category ID in the Categories table should be primary keys.
User ID in the Tasks table and Category ID in the Tasks table should be foreign keys linking to the Users and Categories tables, respectively.

Normalization:
Consider normalizing your tables to avoid data redundancy. For example, you might create a separate Users table to store user information and link tasks to users using their unique User IDs.

Indexing:
Depending on your application's query patterns, you may want to consider indexing certain columns, such as User ID and Category ID, to improve query performance.

Data Integrity Constraints:
Define any necessary data integrity constraints. For example, ensure that a task cannot be assigned to a non-existent user or category.

CLI Commands:
Plan the CLI commands and options that users will use to interact with your Task Manager. For example:

add-task: Adds a new task with specified details.
view-tasks: Displays a list of tasks, optionally filtered by category or priority.
update-task: Allows users to update task details.
delete-task: Removes a task from the database.
add-category: Adds a new category for task classification.

Algorithm for Sorting:
Decide on the algorithm you will use to sort tasks based on priority or due date. You may want to implement sorting methods for tasks when users request them.
