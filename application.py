from flask import Flask, request
import ast
application = Flask(__name__)


def add(a, b):
    return a+b


@application.route('/')
def main():
    return 'API V1.1'


@application.route('/convert', methods=['GET', 'POST'])
def convert():
    if request.method == 'GET':
        return "API V1.1 : /convert [POST]: takes a caracter as input and return  "
    elif request.method == "POST":
        res = ast.literal_eval(request.get_json(force=True))
        data = []
        for i in res:
            data.append(ord(i))
        return str(data)
