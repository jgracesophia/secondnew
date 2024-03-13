from flask import Flask
from werkzeug.urls import quote

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!\n"
