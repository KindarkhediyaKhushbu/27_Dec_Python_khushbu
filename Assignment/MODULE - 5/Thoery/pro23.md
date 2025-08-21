#####  Using Google Maps Geocoding API to convert addresses into coordinates

- Google Maps Geocoding API converts addresses into latitude & longitude.

- Get API Key → from Google Cloud Console.

- Request Example:

https://maps.googleapis.com/maps/api/geocode/json?address=New+York&key=API_KEY


Python Example:
```python
import requests
url = "https://maps.googleapis.com/maps/api/geocode/json"
params = {"address": "New York", "key": "API_KEY"}
res = requests.get(url, params=params).json()
coords = res["results"][0]["geometry"]["location"]
print(coords["lat"], coords["lng"])
```