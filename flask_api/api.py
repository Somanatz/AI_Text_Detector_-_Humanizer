from flask import Flask, request, jsonify
import joblib
import os
import sys


# Get the directory of the current script
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from converter.convert import convert_to_human
model_path = os.path.join(BASE_DIR, "detector", "model.pkl")

# Load full pipeline model
pipeline = joblib.load(model_path)

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    prediction = pipeline.predict([text])[0]
    probability = pipeline.predict_proba([text])[0][1]
    label = "AI-generated" if prediction == 1 else "Human-written"

    return jsonify({
        "prediction": int(prediction),
        "label": label,
        "confidence": round(probability * 100, 2)
    })


@app.route("/convert", methods=["POST"])
def convert():
    data = request.get_json()
    text = data.get("text")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        human_text = convert_to_human(text)
        return jsonify({"converted_text": human_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
