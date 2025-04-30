from flask import Blueprint, jsonify, request
from services.book_service import BookService

book_bp = Blueprint("books", __name__, url_prefix="/v2")


@book_bp.route("/books", methods=["GET"])
def get_books():
    books = BookService.get_all_books()
    return jsonify([book.to_dict() for book in books])


@book_bp.route("/books/<string:book_id>", methods=["GET"])
def get_book(book_id):
    book = BookService.get_book_by_book_id(book_id)
    if book:
        return jsonify(book.to_dict())
    return jsonify({"error": "Book not found"}), 404


@book_bp.route("/books", methods=["POST"])
def add_product():
    data = request.json
    if not data:
        return jsonify({"error": "Payload cannot be empty"}), 400

    books = BookService.create_book(data)
    if not isinstance(books, list):
        return jsonify(books)

    response = {
        "message": "Book successfully created",
        "books": [book.to_dict() for book in books]
    }
    return jsonify(response), 201


@book_bp.route("/api/books/<string:book_id>", methods=["PUT"])
def update_book(book_id):
    new_data = request.json
    if not new_data:
        return jsonify({"error": "The payload cannot be empty"}), 400

    success, updated_book = BookService.update_book(book_id)
    if success:
        return jsonify({"status": "Book successfully updated", "book": updated_book}), 200

    return jsonify({"error": f"Book not found with book_id {book_id}"}), 404


@book_bp.route("/books/<string:book_id>", methods=["DELETE"])
def delete_book(book_id):
    result, books = BookService.delete_book(book_id)

    if not result:
        return jsonify({"error": "Book not found"}), 400

    response = {
        "message": f"Book with book_id {book_id} successfully deleted",
        "books": [book.to_dict() for book in books]
    }

    return jsonify(response)
