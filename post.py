import requests
import pandas as pd
import pprint
import json
import sqlalchemy
from sqlalchemy import create_engine
import matplotlib.pyplot as plt


def main():
    dictarr = portlandPrint(portlandInfo())#[weather]
    dictarr1 = miamiPrint(miamiInfo())#[weather1]
    pprint.pprint(dictarr)
    pprint.pprint(dictarr1)

    # turn dictionary of Portland into JSON file
    with open("weatherPortland.json", "w") as outfile:
        json.dump(dictarr, outfile)
    # turn dictionary of Miami into JSON
    with open("weatherMiami.json", "w") as outfile:
        json.dump(dictarr1, outfile)
    # open JSON file and make it a dataframe PORTLAND
    data = json.load(open('weatherPortland.json'))
    df = pd.DataFrame(
        data["main"], columns=['temp', 'humidity', 'feels_like'], index=[0])
    # open JSON file and make it a dataframe MIAMI
    data1 = json.load(open('weatherMiami.json'))
    df1 = pd.DataFrame(
        data1["main"], columns=['temp', 'humidity', 'feels_like'], index=[0])
    df = df.append(df1, ignore_index=True)
    df.insert(2, "name", ["Portland", "Miami"], True)
    df["temp"] = pd.to_numeric(df["temp"])/10
    df["feels_like"] = pd.to_numeric(df["feels_like"])/10

    print(df)
    barChart(df)
    engine = create_engine('mysql://root:codio@localhost/weather')
    df.to_sql('info', con=engine, if_exists='replace', index=False)

def portlandInfo():
    # Portland
    base = 'http://api.openweathermap.org/'
    route1 = 'data/2.5/weather?q=Portland,%20us&'
    route2 = 'appid=382a88e893bb013cca439718beab4f51'
    url = base + route1 + route2
    return url

def miamiInfo():
    # Miami
    base1 = 'http://api.openweathermap.org/'
    route11 = 'data/2.5/weather?q=Miami,%20us&'
    route22 = 'appid=382a88e893bb013cca439718beab4f51'
    url1 = base1 + route11 + route22
    return url1

def portlandPrint(url):
    # Portland
    r = requests.get(url)
    weather = r.json()
    print("Weather in Portland")
    print(weather['weather'][0]['description'].upper())
    print("Current Temperature: ", weather['main']['temp']//10)
    print("Feels like: ", weather['main']['feels_like']//10)
    print("Max Temperature: ", weather['main']['temp_max']//10)
    print("Humidity: ", weather['main']['humidity'], "\n")
    return weather

def miamiPrint(url1):
    # Miami
    r1 = requests.get(url1)
    weather1 = r1.json()
    print("Weather in Miami")
    print(weather1['weather'][0]['description'].upper())
    print("Current Temperature: ", weather1['main']['temp']//10)
    print("Feels like: ", weather1['main']['feels_like']//10)
    print("Max Temperature: ", weather1['main']['temp_max']//10)
    print("Humidity: ", weather1['main']['humidity'], "\n")
    return weather1
  
def barChart(df):
    x_axis = df["name"]
    y_axis = df["temp"]
    plt.bar(x_axis, y_axis, color=['pink', 'blue'])
    plt.title("Weather")
    plt.xlabel("City")
    plt.ylabel("Fahrenheit")
    plt.show()

if __name__ == '__main__':
    main()
