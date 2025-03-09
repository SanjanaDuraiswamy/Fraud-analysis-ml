 # Credit Card Fraud Detection

This project implements a Credit Card Fraud Detection system using Support Vector Machine (SVM) and Decision Tree classifiers. The model predicts whether a transaction is fraudulent based on extracted features.The model is deployed using Flask, allowing real-time fraud predictions via a web API.

## Dataset Information
- The dataset consists of anonymized transaction data with 30 features.
- **Important:** The first feature (Amount) is not required for prediction and should be removed before feeding data to the model.

## Technologies Used
- Python
- Flask (for API deployment)
- Scikit-learn (SVM & Decision Tree models)
- NumPy & Pandas (for data handling)

## API Usage
1. Run the Flask app:
   ```sh
   python app.py
   ```
2. Make a prediction request via URL:
   ```sh
   http://127.0.0.1:5000/predict?features=value1&features=value2&...
   ```
   - Ensure that exactly **29 features** are passed (excluding the Amount column).

## Example Response
```json
{
  "Decision Tree Prediction": "Not Fraud",
  "SVM Prediction": "Fraud"
}
```

## Repository Structure
- `app.py` - Flask API for fraud detection
- `model.pkl` - Serialized trained model
- `requirements.txt` - Dependencies for running the project

## How to Run
1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Run the Flask app and test predictions using the API.

---
