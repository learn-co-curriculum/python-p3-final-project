# Phase 3 Project: CLI

## Learning Goals

- Configure environments with project-specific parameters using Pipenv.
- Import and use external libraries.
- Use SQLAlchemy ORM and Alembic to create a database schema and update it as you
  continue to build your CLI.
- Use SQLAlchemy ORM to join multiple tables to each other using one-to-one,
  one-to-many, many-to-many relationships.
- Use `list`s, `dict`s, and `tuple`s in appropriate contexts.
- Exercise best practices in CLI design.

***

## Key Vocab

- **Command Line**: a text-based interface that is built into your computer's
operating system. It allows you to access the files and applications on your
computer manually or through scripts.
- **Terminal**: the application in Mac OS that allows you to access the command
line.
- **Command Shell/Powershell**: the applications in Windows that allow you to access
the command line.
- **Command-Line Interface (CLI)**: a text-based interface used to run programs,
manage files and interact with objects in memory. As the name suggests, it is
run from the command line.

***

## Instructions

Welcome to the end of Phase 3! You've learned about a lot in this unit:

- Python fundamentals.
- Data structures (and more recently, algorithms).
- Object-oriented programming.
- Object inheritance.
- Class attributes and methods.
- Configuring applications.
- SQL fundamentals.
- Table relations in SQL.
- Object-relational mapping with Python.
- Object-relational mapping with SQLAlchemy.
- Building CLIs.

In this project, we're going to use these skills to create a CLI. We want you to
display knowledge of as much from Phase 3 as you can- you won't be able to fit
everything in, but we'll expect to see:

- A CLI application that solves a real-world problem and adheres to best
  practices.
- A database created and modified with SQLAlchemy ORM with 3+ related tables.
- A well-maintained virtual environment using Pipenv.
- Proper package structure in your application.
- Use of `list`s, `dict`s, and `tuple`s.

A rubric for this project is available on the next page in this Canvas module.
Make sure to take a look before you get started!

***

## Tips and Tricks?

- Think about your database schema before you begin- migrations are a pain!
- Keep your Python objects, SQLAlchemy objects, and CLI script in separate
  modules.
- If you get stuck trying to accomplish a specific task, check online to see if
  there's a Python library that will make it easier.
- Consider using [Click][click] or [Fire][fire] to take care of basic CLI tasks
  for you.

***

## Resources

- [Click documentation][click]
- [The Python Fire Guide][fire]

[click]: https://click.palletsprojects.com/en/8.1.x/
[fire]: https://google.github.io/python-fire/guide/
