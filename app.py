
import flask
from flask import jsonify,request

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

app = flask.Flask(__name__)

#function to send mail
def send_mail(body):
    
    email = 'q4t14all@gmail.com'
    password = 'rkv#3117'
    send_to_email = 'crizal501@gmail.com'
    subject = 'Test'
    message = body
    
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject
    
    
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    server.quit()
    return "Mail Sent"






@app.route('/')
def home():
    return "Hello, World! new"

@app.route('/add/<int:a>/<int:b>',methods=['GET','POST'])
def add(a,b):
    sum = str(a+b)
    return jsonify({'sum': sum})

@app.route('/sms/<int:id>',methods=['GET','POST'])
def sms(id):
    if request.method == 'POST':
        content = request.json
        send_mail(content)
        return content
    # content = request.json
    # print(content)
    # return content

if __name__ == '__main__':
    app.run()

  