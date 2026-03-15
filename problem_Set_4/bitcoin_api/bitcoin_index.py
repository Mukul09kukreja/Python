import requests

api = "96665cb5e9578163e96784373a8ca0c30050c7167baf77bb13992c50f1c51b46"

url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api}"

response = requests.get(url)
data = response.json()
print(data)