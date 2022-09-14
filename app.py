import flask
from flask import jsonify
app = flask.Flask(__name__)

@app.route('/<int:a>/<int:b>')
def add(a,b):
    sum = str(a+b)
    return jsonify({'sum': sum})

if __name__ == '__main__':
    app.run()
    
  