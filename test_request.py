import requests

url = "http://127.0.0.1:5000/predict"
payload = {
    "user_id": 5,
    "amount": 100000,
    "location": "RU",
    "device": "Linux"
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response:", response.json())

