import requests

url = "http://127.0.0.1:5000/predict"
data = {"features": [0.1, 0.5, -1.2, 3.0]}  # Replace with actual feature values

response = requests.post(url, json=data)
print(response.json())  # See the prediction output
