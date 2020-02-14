# -*- coding: utf-8 -*-
__author__ = 'nobita'


from flask import Flask, request
from mail_process import extract_mail
app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')

@app.route('/', methods = ['GET'])
def homepage():
    return app.send_static_file('index.html')


@app.route('/ner', methods=['POST'])
def process_request():
    data = request.form['data']
    print(u'Input:\n%s' % (data))
    result = extract_mail(data)
    print(u'Result:\n%s' % (result))
    return result



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)