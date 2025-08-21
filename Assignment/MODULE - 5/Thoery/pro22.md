##### • Introduction to OpenWeatherMap API and how to retrieve weather data.
OpenWeatherMap API provides real-time weather data via REST API.
```python
Python Example:

import requests
res = requests.get("https://api.openweathermap.org/data/2.5/weather",
                   params={"q": "London", "appid": "API_KEY", "units": "metric"})
data = res.json()
print(data["main"]["temp"], data["weather"][0]["description"])
```