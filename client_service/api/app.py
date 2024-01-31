from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/books', methods=['GET'])
def get_books():
    id_query = request.args.get('id', default='', type=int)
    author_query = request.args.get('author', default='', type=str)
    genre_query = request.args.get('genre', default='', type=str)
    response = requests.get('http://sse-lab10-book-api.edhehtb8echmdte6.uksouth.azurecontainer.io:5000')
    books = response.json()

    if id_query:
        filtered_books = [book for book in books if id_query == book['id']]
        return jsonify(filtered_books)
    
    if author_query:
        filtered_books = [book for book in books if author_query.lower() in book['author'].lower()]
        return jsonify(filtered_books)
    
    if genre_query:
        filtered_books = [book for book in books if genre_query.lower() in book['genre'].lower()]
        return jsonify(filtered_books)

    return jsonify(books)