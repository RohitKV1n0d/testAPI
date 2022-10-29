
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
        msg = str(content["content"])
        otp = msg[61:67]
        with open("otp.txt", "w") as outfile:
            outfile.write(otp)
        
        return 'success'
    
    f = open("otp.txt", "r")

    data = f.read()
    return "<h1> {}</h1>".format(data)

@app.route('/getotp',methods=['GET','POST'])
def getotp():
    f = open("otp.txt", "r")

    data = f.read()

   
    return jsonify({'otp': data})


if __name__ == '__main__':
    app.run()

  