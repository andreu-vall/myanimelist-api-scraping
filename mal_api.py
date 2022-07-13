import requests

api_url = 'https://api.myanimelist.net/v2'

# A Client ID is needed (https://myanimelist.net/apiconfig)
with open('client_id.txt', 'r') as f:
    CLIENT_ID = f.read()

headers = {'X-MAL-CLIENT-ID': CLIENT_ID}

def get_data(endpoint, params=None):
    url = api_url + endpoint
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()