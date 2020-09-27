from flask import Blueprint, jsonify, request, render_template
from web_app.models import Book, db, parse_records

book_routes = Blueprint("book_routes", __name__)

@book_routes.route("/books.json")
def list_books():
    book_records = Book.query.all()
    print(book_records)
    books = parse_records(book_records)
    return jsonify(books)

@book_routes.route("/books")
def list_book_for_humans():
    book_records = Book.query.all() # returns the books in the database
    print(book_records)
    books = parse_records(book_records)
    return render_template("books.html", message="Here's some books", books=books)

@book_routes.route("/books/new")
def new_book():
    return render_template("new_book.html")

@book_routes.route("/books/create", methods=["POST"])
def create_book():
    print("FROM DATA:", dict(request.form))
    
    new_book = Book(title=request.form["book_title"], author_id=request.form["author_name"])
    db.session.add(new_book)
    db.session.commit()

    return jsonify({
        "message": "BOOK CREATED OK (todo)",
        "book": dict(request.form)
    })