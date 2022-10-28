
import flask
from flask import jsonify,request


import json


app = flask.Flask(__name__)







@app.route('/')
def home():
    return "Hello, World! new"

@app.route('/add/<int:a>/<int:b>',methods=['GET','POST'])
def add(a,b):
    sum = str(a+b)
    return jsonify({'sum': sum})

@app.route('/sms',methods=['GET','POST'])
def sms():
    if request.method == 'POST':
        content = request.json

        
        json_object = json.dumps(content)
        with open("json.txt", "w") as outfile:
            outfile.write(json_object)
        
        f = open("json.txt", "r")

        data = f.read()
        
        return '''
        <h1>The content is {}</h1>'''.format(data)
    
    f = open("json.txt", "r")

    data = f.read()
    return "<h1> {}</h1>".format(data)


if __name__ == '__main__':
    app.run()

  