import time
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "hello to my sample flask ap"
