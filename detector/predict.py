import joblib
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Load the full pipeline model
pipeline = os.path.join(BASE_DIR, "detector", "model.pkl")
#model_path = os.path.join(BASE_DIR, "detector", "model.pkl")

def detect_ai_text(text):
    # Predict probability using the pipeline directly
    prob = pipeline.predict_proba([text])[0][1]
    label = "AI-Generated" if prob > 0.5 else "Human-Written"
    return label, prob
