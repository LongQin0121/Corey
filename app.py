import requests

# Replace 'YOUR_API_KEY' with the API key you obtained from Open Exchange Rates
api_key = 'YOUR_API_KEY'
url = f'https://open.er-api.com/v6/latest/{api_key}'

# Make a GET request to the Open Exchange Rates API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Print the data
    print(data)
else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code}")
