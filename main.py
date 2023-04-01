#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify
from sprc_connector import get_sparc_result
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/query_sparc1', methods=['GET'])
def get_query_records():
    input_string = request.args.get('input_string')
    try:
        query = get_sparc_query(input_string)
        result = get_sparc_result(query)
        return jsonify({'result': result})
    except Exception as err:
        return jsonify({'error': 'data not found', "reason": str(err)})


@app.route('/query_sparc', methods=['POST'])
def post_query_records():
    input_string = request.form.get('query')
    try:
        query = get_sparc_query(input_string)
        result = get_sparc_result(query)
        response = jsonify({'result': result})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as err:
        return jsonify({'error': 'data not found', "reason": str(err)})


def get_sparc_query(input_string):
    # Todo need to implement som AI work to map query and input string

    if 'borrow' in input_string and 'book' in input_string:
        book_type = 'General books'
        return f"borrowing_period('{book_type}', B) :- book('book1', '{book_type}'). #maximize {{ B }}. #show B : borrowing_period('{book_type}', B), book('book1', '{book_type}')."
    elif 'lost' in input_string and 'book' in input_string:
        return "lost_book_policy(P) :- #show P : lost_book_policy(P)."
    else:
        return None
    return 'opening_hours(weekday,X)'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
