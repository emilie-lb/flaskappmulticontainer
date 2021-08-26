#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask_cors import CORS
from flask import Flask, jsonify, request
# from flaskext.mysql import MySQL
# import logging
# import back.fonctions as fc
# # import fonctions as fct

app = Flask(__name__)
CORS(app)

#logging.basicConfig(level=logging.DEBUG)


@app.route('/', methods=['GET', 'POST'])
def entry_point():
  """docstring zfzef zefzafza zvzeveza"""
  return "Hello"

@app.route('/hello_world')
def hello_world():
  """docstring zfzef zefzafza zvzeveza"""
  return 'Hello World'

@app.route('/login', methods=['GET', 'POST'])
def login():
    station = request.args.get('station') +'ttttt'
    destination = request.args.get('destination') + 'ttttt'
    passage = [station, destination]
    return jsonify(passage)


# if __name__ == '__main__':
#   # app.config.update(ENV="development", DEBUG=True)
#   # app.run(host="0.0.0.0")
#   app.run(debug=True)
