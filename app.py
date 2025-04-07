from flask import Flask, jsonify, request, render_template
from controllers.book_controller import book_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(book_bp)

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"error": "Bad Request"}), 400
    
    @app.errorhandler(404)
    def bad_request(error):
        return jsonify({"error": "Not Found"}), 404
    
    @app.errorhandler(500)
    def bad_request(error):
        return jsonify({"error": "Internal Service Error"}), 500

    return app









if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
