from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "outputs", "lgbm_model.pkl")
model = joblib.load(MODEL_PATH)

app = Flask(__name__)

@app.route("/")
def home():
    return "IoT Predictive Maintenance API is Running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    input_df = pd.DataFrame([data])

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    result = {
        "prediction": int(prediction),
        "failure_probability": round(float(probability * 100), 2)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)