
from http import server
import flask
from flask import jsonify,request

import smtplib


app = flask.Flask(__name__)

# #function to send mail
# def send_mail(body):
    
    





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
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("testsmsforwarding@gmail.com", "Test@123sms")
        server.sendmail("testsmsforwarding@gmail.com", "crizal501@gmail.com", "body")
        server.quit()

        return jsonify({'status': 'success'})
    # content = request.json
    # print(content)
    # return content

if __name__ == '__main__':
    app.run()

  