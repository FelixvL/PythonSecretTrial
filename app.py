from flask import Flask
from decouple import config

app = Flask(__name__)



@app.route("/")
def hello_world():
    geheim = "hoidaar"
    return "<p>Hello, World!</p>" + geheim