import requests

base = 'http://api.openweathermap.org/'
route1 = 'data/2.5/weather?q=Portland,%20us&'
route2 = 'appid=382a88e893bb013cca439718beab4f51'
url = base + route

r = requests.get(url)
weather = r.json()
print("Weather in Portland")
print(weather['weather'][0]['description'].upper())
print("Current Temperature: ", weather['main']['temp']//10)
print("Feels like: ", weather['main']['feels_like']//10)
print("Max Temperature: ", weather['main']['temp_max']//10)
print("Humidity: ", weather['main']['humidity'], "\n")
