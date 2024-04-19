
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, tWorld!</p>"

@app.route("/wpwwwwww", methods=['GET','POST'])
def hello_w():
    if request.method =='POST':
        payload = {'message':'post'}
        print(payload)
        return jsonify(payload)
    payload = {'message':'get'}
    print(payload)
    return jsonify(payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)