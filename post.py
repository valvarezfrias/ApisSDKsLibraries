import requests
import pandas as pd
import pprint
import json
import sqlalchemy
from IPython.display import display, HTML
from sqlalchemy import create_engine

# Portland
base = 'http://api.openweathermap.org/'
route1 = 'data/2.5/weather?q=Portland,%20us&'
route2 = 'appid=382a88e893bb013cca439718beab4f51'
url = base + route1 + route2

# Miami
base1 = 'http://api.openweathermap.org/'
route11 = 'data/2.5/weather?q=Miami,%20us&'
route22 = 'appid=382a88e893bb013cca439718beab4f51'
url1 = base1 + route11 + route22

# Portland
r = requests.get(url)
weather = r.json()
print("Weather in Portland")
print(weather['weather'][0]['description'].upper())
print("Current Temperature: ", weather['main']['temp']//10)
print("Feels like: ", weather['main']['feels_like']//10)
print("Max Temperature: ", weather['main']['temp_max']//10)
print("Humidity: ", weather['main']['humidity'], "\n")

# Miami
r1 = requests.get(url1)
weather1 = r1.json()
print("Weather in Miami")
print(weather1['weather'][0]['description'].upper())
print("Current Temperature: ", weather1['main']['temp']//10)
print("Feels like: ", weather1['main']['feels_like']//10)
print("Max Temperature: ", weather1['main']['temp_max']//10)
print("Humidity: ", weather1['main']['humidity'], "\n")

dictarr = [weather]
dictarr1 = [weather1]
pprint.pprint(dictarr)
pprint.pprint(dictarr1)

# turn dictionary of Portland into JSON file
with open("weatherPortland.json", "w") as outfile:
    json.dump(weather, outfile)
# turn dictionary of Corvallis into JSON
with open("weatherMiami.json", "w") as outfile: 
    json.dump(weather1, outfile)
# open JSON file and make it a dataframe PORTLAND
data = json.load(open('weatherPortland.json'))
df = pd.DataFrame(
    data["weather"], columns=['id', 'main', 'description', 'icon'])
# open JSON file and make it a dataframe MIAMI
data1 = json.load(open('weatherMiami.json'))
df1 = pd.DataFrame(
    data1["weather"], columns=['id', 'main', 'description', 'icon'])
df = df.append(df1, ignore_index=True)

display(df)
engine = create_engine('mysql://root:codio@localhost/weather')
df.to_sql('info', con=engine, if_exists='replace', index=False)
