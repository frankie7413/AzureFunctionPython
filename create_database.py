"""Create database for development and testing"""
from sqlalchemy import inspect
from sqlalchemy_utils import database_exists, create_database
from models.base import engine, init_db

if not database_exists(engine.url):
    print('Creating database from scratch.')
    create_database(engine.url)

if database_exists(engine.url):
    print('Database Created Successfully')
else:
    print('Error in creating Database')

init_db()

print(f"Tables created: {inspect(engine).get_table_names()}")
