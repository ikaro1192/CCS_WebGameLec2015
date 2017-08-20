#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine


from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

class User(object):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

@app.route('/scores', methods=['GET', 'POST'])
def scores_view():
    result = ''

    if request.method == 'POST':
        result = post_score()
    if request.method == 'GET':
        result = get_score(request)

    return result

def post_score():
    return 'POST'

def get_score(request):
    limit = request.args.get('limit')
    if limit is None:
        limit = '10'
    return limit

if __name__ == '__main__':
    app.run(debug=True)
