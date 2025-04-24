from db import book_data
from models.book_model import Book


class BookService:

    @staticmethod
    def get_all_books():
        return book_data

    @staticmethod
    def get_book_by_book_id(book_id):
        for book in book_data:
            if book.book_id == book_id:
                return book
        return None

    @staticmethod
    def create_book(data: dict):

        if not data.get("book_id"):
            return {"book_id": "book_id is required"}

        if not data.get("author"):
            return {"author": "author is required"}

        if not data.get("title"):
            return {"title": "title is required"}

        if not isinstance(data.get("book_id"), str):
            return {"book_id": "book_id should be a string"}

        if not isinstance(data.get("title"), str):
            return {"title": "title should be a string"}

        if not isinstance(data.get("author"), str):
            return {"author": "author should be a string"}

        if not isinstance(data.get("rating"), float):
            return {"rating": "rating should be a float"}

        if not isinstance(data.get("publication_year"), int):
            return {"publication_year": "publication_year should be a intiger"}

        if not data.get("book_id").startswith("B_"):
            return {"book_id": f"book_id {data.get("book_id")} should starts with B_"}

        valid_status = ["read", "reading", "to-read"]
        if data.get("read_status") not in valid_status:
            return {"read_status": "read_status must be read, reading or to-read"}

        if data.get("rating") < 0 or data.get("rating") > 5:
            return {"rating": "rating must be float in 0-5"}

        for book in book_data:
            if book.book_id == data.get("book_id"):
                return {"book_id": f"book_id {data.get("book_id")} already exists"}

        new_book = Book(
            book_id=data.get("book_id"),
            author=data.get("author"),
            title=data.get("title"),
            publication_year=data.get("publication_year"),
            rating=data.get("rating"),
            read_status=data.get("read_status"),
            genre=data.get("genre"),
            notes=data.get("notes")
        )

        book_data.append(new_book)
        return book_data

    # @staticmethod
    # def update_book(book_id):
    #     for book in book_data:
    #         if book.book_id == book_id:
    #             book_data.update(book)
    #             return True, book_data
    #     return False, None

    @staticmethod
    def delete_book(book_id):
        for book in book_data:
            if book.book_id == book_id:
                book_data.remove(book)
                return True, book_data
        return False, None
