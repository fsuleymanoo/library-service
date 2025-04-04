from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


books = [
    {"book_id": "001", "title": "JAVA", "author": "John Doe", "publication_year": 2000,
        "genre": "coding", "read_status": "read", "rating": 3.5, "notes": "do not read again"},
    {"book_id": "002", "title": "JS", "author": "Mark", "publication_year": 2004,
     "genre": "coding", "read_status": "reading", "rating": 4.5, "notes": "read again"}
]

stats = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/books/", methods=["GET"])
def get_books():
    return jsonify(books), 200


@app.route("/api/books/<string:book_id>/", methods=["GET"])
def get_single_book(book_id):
    for book in books:
        if book_id == book.get("book_id"):
            return jsonify(book), 200
    return jsonify({"error": f"Book not found with book_id {book_id}"}), 404


@app.route("/api/books", methods=["POST"])
def add_book():
    new_book = request.json
    if not new_book:
        return jsonify({"error": "The payload cannot be empty"}), 400
    if "book_id" not in new_book or "title" not in new_book or "author" not in new_book:
        return jsonify({"error": "Missing required fields (book_id, title, author)"}), 400
    rating = float(new_book["rating"])
    if rating < 0 or rating > 5:
        return jsonify({"error": "rating range 0-5"}), 400
    valid_status = ["read", "reading", "to-read"]
    if new_book["read_status"] not in valid_status:
        return jsonify({"error": "valid read_status (read, reading, to-read)"}), 400
    for book in books:
        if new_book.get("book_id") == book.get("book_id"):
            return jsonify({"error": f"book_id is already present"}), 400
    books.append(new_book)
    return jsonify({"status": "Book successfully added", "books": books}), 201


@app.route("/api/books/<string:book_id>", methods=["PUT"])
def update_book(book_id):
    book_update = None
    for book in books:
        if book_id == book.get("book_id"):
            book_update = book
    if book_update:
        new_book = request.json
        book_update.update(new_book)
        return jsonify({"status": "Book successfully updated", "books": books}), 200

    return jsonify({"error": f"Book not found with book_id {book_id}"}), 404


@app.route("/api/books/<string:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book_delete = None
    for book in books:
        if book_id == book.get("book_id"):
            book_delete = book
    if book_delete:
        books.remove(book_delete)
        return jsonify({"status": "Book successfully deleted", "books": books}), 200

    return jsonify({"error": f"Book not found with book_id {book_id}"}), 404


@app.route("/api/books/stats", methods=["GET"])
def get_stats():
    ratings = [float(book.get("rating", 0))
               for book in books if "rating" in book]
    average_rating = round(sum(ratings) / len(ratings), 2) if ratings else 0.0
    read_books = [book for book in books if book.get("read_status") == "read"]
    return jsonify({"total_books": len(books), "books_read": len(read_books), "average_rating": average_rating}), 200


if __name__ == "__main__":
    app.run(debug=True)
