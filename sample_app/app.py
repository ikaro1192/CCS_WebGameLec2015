#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/scores', methods=['GET', 'POST'])
def scores_view():
    result = ''

    if request.method == 'POST':
        result = post_scores()
    if request.method == 'GET':
        result = get_scores()

    return result

def post_scores():
    return 'POST'

def get_scores():
    return 'GET'

if __name__ == '__main__':
    app.run(debug=True)
