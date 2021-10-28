# Puller functions
import bs4
import requests
import os
import os.path

with open(os.path.dirname(__file__) + "/../web_data/puller.py", "r") as puller:
    data = puller.read()
with open("puller.py", "w+") as file:
    file.write(data)
from puller import *
os.remove("puller.py")

test_url = "https://www.york.ac.uk/teaching/cws/wws/webpage1.html"


weather_url = "https://www.wunderground.com/weather/us/ca/alturas"
temperature_element = "wu-value wu-value-to"
feels_like_element = ""


def get_weather(weather_url=weather_url):
    return get_webpage(weather_url)


def get_temp(url=weather_url, page=""):
    if not bool(page):
        page = get_webpage(url)
    return str(find_element(temperature_element, webpage=page).contents[0])


def get_feels_like(url=weather_url, page=""):
    if not page:
        page = get_webpage(url)
    soup = bs4.BeautifulSoup(page, features="html.parser")
    return str(bs4.BeautifulSoup(str(soup.findChildren(class_="feels-like")), features="html.parser").find(class_="temp").contents[0].replace("°", ""))


def get_precipitation(url=weather_url, page=""):
    if not page:
        page = get_webpage(url)
    soup = bs4.BeautifulSoup(page, features="html.parser")
    return float(soup.find(type="rain").find(class_="wu-value wu-value-to").contents[0])


def test():
    """
    print(get_feels_like())
    print(get_temp())"""

    print(get_precipitation())


if __name__ == '__main__':
    test()
