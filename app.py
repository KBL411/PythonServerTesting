import flask
import numpy as np
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    return "hello to my flask app, to test the mean function copy/paste this in tour webrowser\n " \
           "localhost:5000/mean?list=1&list=2&list=3&list=4 "


@app.route('/mean', methods=['GET'])
def mean():
    da_list = request.args.getlist("list", type=int)
    list_mean = np.mean(da_list)
    return "The list: '{}' \n The mean '{}'".format(da_list, list_mean)

