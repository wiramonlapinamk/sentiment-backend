
import pickle

import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS  # CORS for handling Cross-Origin Resource Sharing

app = Flask(__name__)
CORS(app,resources={r"/*":{"origins":"*"}})


model = pickle.load(open('ml_model.pkl', 'rb'))

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/predict", methods=['POST'])
def predict():
    try:
        data = request.get_data()
        query_df = ([data])
        prediction = model.predict(query_df)
        print(prediction)
        return jsonify({'message' : list(prediction)})
    except Exception as e:
        return jsonify({'error':str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)