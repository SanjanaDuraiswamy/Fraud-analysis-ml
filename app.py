from flask import Flask, request, jsonify
import numpy as np
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load trained models
dt_model = joblib.load("decision_tree.pkl")
svm_model = joblib.load("svm_model.pkl")

@app.route('/')
def home():
    return "Credit Card Fraud Detection API is Running!"

@app.route('/predict', methods=['GET'])
def predict():
    try:
        # Get feature values from URL parameters
        features = request.args.getlist("features", type=float)

        if not features:
            return jsonify({"error": "No features provided. Use /predict?features=value1&features=value2&..."})
        
        # Convert to NumPy array and reshape
        features_array = np.array(features).reshape(1, -1)

        # Predict using Decision Tree
        dt_prediction = dt_model.predict(features_array)[0]
        
        # Predict using SVM
        svm_prediction = svm_model.predict(features_array)[0]

        return jsonify({
            "Decision Tree Prediction": "Fraud" if dt_prediction == 1 else "Not Fraud",
            "SVM Prediction": "Fraud" if svm_prediction == 1 else "Not Fraud"
        })
    
    except Exception as e:
        return jsonify({"error": str(e)})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
