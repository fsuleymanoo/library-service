from db import get_db
from psycopg2.extras import RealDictCursor


class BookRepository:

    @staticmethod
    def get_all_books():
        connection = get_db()
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                # select
            )
            cursor.fetchall()