import os
import discord
from bs4 import BeautifulSoup
import requests


url = "https://www.google.com/search?q=weather+in+"

headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

##we can store the information we scrape into a location class
class Location:

    def __init__(self, name, temperture, humdity, windspeed):
        self.name = name
        self.temperature = temperture
        self.humidty = humdity
        self.windspeed = windspeed

    def toString(self):
        return "Location: " + self.name + " ||  Temperature: " + self.temperature + "°C || " + "Humidity: " + self.humidty + " || Windspeed: " + self.windspeed




## the actual script is here
def weather(str):


    result = requests.get(url + str, headers=headers, cookies = {'CONSENT' : 'YES+'})
    doc = BeautifulSoup(result.text, "html.parser")
    divs = doc.find_all("div",class_="wob_t")
    tmp = doc.find_all("span", class_="wob_t")
    precipitation = doc.find_all("span", id="wob_pp")
    humidity = doc.find_all("span", id="wob_hm")
    windspeed = doc.find_all("span", id="wob_ws")
    location = doc.find_all("div", id="wob_loc")

    loc = Location(location[0].string, tmp[0].string, humidity[0].string, windspeed[0].string)
    print(loc.toString())




if __name__ == '__main__':

    while True:
        print("please enter a city: ")
        city = input()
        weather(city)
