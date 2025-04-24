from uuid import uuid4
from datetime import datetime


class Book:
    def __init__(self, book_id, author, genre, notes, publication_year, rating, read_status, title, uuid=None, created_at=None, **kwargs):
        self.book_id = book_id
        self.author = author
        self.genre = genre
        self.notes = notes
        self.publication_year = publication_year
        self.rating = rating
        self.read_status = read_status
        self.title = title
        self.uuid = uuid if uuid else str(uuid4())
        self.created_at = created_at if created_at else datetime.now()

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "author": self.author,
            "genre": self.genre,
            "notes": self.notes,
            "publication_year": self.publication_year,
            "rating": self.rating,
            "read_status": self.read_status,
            "title": self.title,
            "uuid": self.uuid,
            "created_at": self.created_at
        }
