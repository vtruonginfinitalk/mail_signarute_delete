# -*- coding: utf-8 -*-

""" Documentation for my module. With **formatting**. """
import json
import pprint

from flask import Flask, request

import analysis.sentiment_analysis as sentiment_analysis

# pylint: disable=invalid-name
app = Flask(__name__)

def response_error(response_code, message, errors = {}):
    """ Documentation for my module. With **formatting**. """
    response_data = {
        "message": message,
        "status": False,
        "errors": errors,
    }

    response = app.response_class(
        status=response_code,
        response=json.dumps(response_data),
        mimetype='application/json'
    )

    return response
def response_success(response_code, data):
    """ Documentation for my module. With **formatting**. """
    response_data = {
        "data": data,
        "status": True,
    }

    response = app.response_class(
        status=response_code,
        response=json.dumps(response_data),
        mimetype='application/json'
    )

    return response

@app.route('/analysis/sentiment', methods=['GET'])
def home():
    """ Documentation for my module. With **formatting**. """

    pprint.pprint(request)
    data = request.args
    if 'text' in data:
        text = str(data['text'])
    else:
        response = response_error(400, 'NO_PARAM_TEXT_IN_REQUEST')
        return response
    try:
        result = sentiment_analysis.sample_analyze_sentiment(text)
    except Exception as inst:
        return response_error(500, 'SERVER_ERROR', inst)

    return response_success(200, result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
