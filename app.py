
from operator import concat
import flask
from flask import jsonify,request
app = flask.Flask(__name__)


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
        return jsonify({'id': id})
    # content = request.json
    # print(content)
    # return content

if __name__ == '__main__':
    app.run()

  