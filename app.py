from flask import Flask, request, jsonify
from fraud_model import FraudDetector
import pandas as pd

app = Flask(__name__)
detector = FraudDetector()

# Train on startup using sample data
df = pd.read_csv("test_data.csv")
detector.train(df)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    result = detector.predict(data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)