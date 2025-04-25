from db import get_db
from psycopg2.extras import RealDictCursor


class BookRepository:

    @staticmethod
    def get_all_books():
        connection = get_db()
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                "SELECT book_id, author, genre, notes, publication_year, rating, read_status, title, uuid, created_at FROM books;"
            )
            return cursor.fetchall()

    @staticmethod
    def get_book_by_book_id(book_id):
        connection = get_db()
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                "SELECT book_id, author, genre, notes, publication_year, rating, read_status, title, uuid, created_at FROM books WHERE book_id = %s;", (book_id,))
            return cursor.fetchone()

    @staticmethod
    def create_book(book):
        connection = get_db()
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("""
                INSERT INTO books (book_id, author, genre, notes, publication_year, rating, read_status, title, uuid, created_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING *           
                """, (
                book.book_id,
                book.author,
                book.genre,
                book.notes,
                book.publication_year,
                book.rating,
                book.read_status,
                book.title,
                book.uuid,
                book.created_at,
            ))
            connection.commit()
            return cursor.fetchone()

    @staticmethod
    def update_book(book_id, book):
        connection = get_db()
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("""
                UPDATE books SET author = %s, genre = %s, notes = %s, publication_year = %s, rating = %s, read_status = %s, title = %s, uuid = %s, created_at = %s WHERE book_id = %s RETURNING *;             
                """, (
                book.author,
                book.genre,
                book.notes,
                book.publication_year,
                book.rating,
                book.read_status,
                book.title,
                book.uuid,
                book.created_at,
                book_id
            ))
            connection.commit()
            return cursor.fetchone()
        

    @staticmethod
    def delete_book(book_id):
        connection = get_db()
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("DELETE FROM books WHERE book_id = %s RETURNING *;", (book_id,))
            deleted = cursor.fetchone()
            print("DELETED: ", deleted)
            connection.commit()
            return deleted    
