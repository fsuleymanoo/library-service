from app import create_app
from db import get_db, close_db


def create_tables():
    app = create_app()

    with app.app_context():
        conn = get_db()
        cur = conn.cursor()
        cur.execute(""" 
            CREATE TABLE IF NOT EXISTS books (
                book_id VARCHAR(64) UNIQUE NOT NULL,
                author VARCHAR(64) NOT NULL,
                genre VARCHAR(64) NOT NULL,
                notes VARCHAR(255), 
                publication_year INT NOT NULL,
                rating DECIMAL NOT NULL,
                read_status VARCHAR(10) NOT NULL,
                title VARCHAR(64) NOT NULL,
                uuid UUID NOT NULL,
                created_at TIMESTAMP NOT NULL                                    
             ) 
                            
        """)
        conn.commit()
        cur.close()
        close_db()


if __name__ == "__main__":
    create_tables()
    print("Table Successfully Created!")
