import requests

url = "https://besttime.app/api/v1/forecasts/live"

params = {
    'api_key_private': 'pri_50990bf1f8828f6abbf6152013113c6b',
    'venue_name': 'McDonalds',
    'venue_address': 'Ocean Ave, San Fransisco'
}

response = requests.request("POST", url, params=params)
print(response.json())