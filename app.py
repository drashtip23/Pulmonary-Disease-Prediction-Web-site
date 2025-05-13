from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from frontend

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Example: List your feature names in order
FEATURES = ['feature1', 'feature2', 'feature3']  # Replace with your actual features

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Extract features in the correct order
    input_data = [data[feature] for feature in FEATURES]
    input_df = pd.DataFrame([input_data], columns=FEATURES)
    prediction = model.predict(input_df)[0]
    return jsonify({'prediction': int(prediction)})

if __name__ == '__main__':
    app.run(debug=True) 