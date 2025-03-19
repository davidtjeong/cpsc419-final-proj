import requests

BASE_URL = "http://127.0.0.1:5000"

params = {'bedrooms': 2,
          'bathrooms': 1,
          'street_address': "Main",
          'price': 1000,
          'square_footage': 800
          }

# Send a GET request
get_response = requests.get(f"{BASE_URL}/api/listings", params=params)

print("Status Code:", get_response.status_code)
print("Response JSON:", get_response.json())


listing_data = {
    'street_address': "test street",
    'city': "test city",
    'state': "test state",
    'zip_code': "test zip",
    'country': "test country",
    'bedrooms': 1,
    'bathrooms': 1,
    'square_footage': 500,
    'title': "Test Listing",
    'price': 1000,
    'description': "This is a test listing",
    'start_date': "2025-01-01",
    'end_date': "2025-12-31",
}

post_response = requests.post(f"{BASE_URL}/api/listings", params=listing_data)

print("Status Code:", post_response.status_code)
print("Response JSON:", post_response.json())
