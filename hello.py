from play import get_pythag
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/pythag', methods=['GET'])
def pythag():
  return jsonify(get_pythag())

