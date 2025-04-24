from models.book_model import Book
book_data = [
    Book(
        book_id="B_001",
        author="John Doe",
        genre="Coding",
        notes="great book",
        publication_year=2005,
        rating=3.9,
        read_status="reading",
        title="OOP"
    ),
    Book(
        book_id="B_002",
        author="Bob Soe",
        genre="true story",
        notes="nice book",
        publication_year=2009,
        rating=1.3,
        read_status="read",
        title="Life"
    ),

]

import psycopg2
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            dbname="flask-book-service",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
