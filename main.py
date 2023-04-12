from flask import Flask, request
import ast
application = Flask(__name__)
app = application
app.config["DEBUG"] = True


@app.route('/', methods=['GET', 'POST'])
def main():
    return 'API V1.0'


@app.route('/convert', methods=['GET', 'POST'])
def convert():
    if request.method == 'GET':
        return "API V1.0 : /convert [POST]: takes a caracter as input and return  "
    elif request.method == "POST":
        res = ast.literal_eval(request.get_json(force=True))

        data = []
        for i in res:
            data.append(ord(i))
        return str(data)


app.run()
