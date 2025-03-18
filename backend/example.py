import requests

BASE_URL = "http://127.0.0.1:5000"

params = {"bedrooms": 2}

# Send a GET request
response = requests.get(f"{BASE_URL}/api/listings", params=params)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
