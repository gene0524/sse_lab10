from flask import Flask, jsonify
from books import books

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify(books)
