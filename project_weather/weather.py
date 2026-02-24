import requests

url = "http://api.weatherapi.com/v1/forecast.json?key=c5f54be9ed804fe893684503262402&q=india&days=1&aqi=yes&alerts=yes"

def weather_info():
  response = requests.get(url)
  if response.status_code == 200:
    weather_data = response.json()
    return weather_data
  

info = weather_info()
print(info['current']['gust_kph'])