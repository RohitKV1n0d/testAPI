from crypt import methods
import flask
from flask import jsonify
app = flask.Flask(__name__)


@app.route('/')
def home():
    return "Hello, World!"

@app.route('/<int:a>/<int:b>',methods=['GET','POST'])
def add(a,b):
    sum = str(a+b)
    return jsonify({'sum': sum})


if __name__ == '__main__':
    app.run()

  