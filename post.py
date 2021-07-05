import requests

url = 'http://api.openweathermap.org/data/2.5/weather?q=Portland,%20us&appid=382a88e893bb013cca439718beab4f51'
r = requests.get(url)
#print(r.status_code)
weather = r.json()
#print(weather)
print("Weather in Portland")
print(weather['weather'][0]['description'].upper())
print("Current Temperature: ", weather['main']['temp']//10)
print("Feels like: ", weather['main']['feels_like']//10)
print("Max Temperature: ", weather['main']['temp_max']//10)
print("Humidity: ", weather['main']['humidity'])