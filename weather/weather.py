import os
import bs4
import puller


weather_url = "https://www.wunderground.com/weather/us/ca/alturas"
temperature_element = "wu-value wu-value-to"
feels_like_element = ""


def get_temp(url=weather_url, page=""):
    if not bool(page):
        page = puller.get_webpage(url)
    return puller.find_element(temperature_element, webpage=page).contents[0]


def get_feels_like(url=weather_url, page=""):
    if not page:
        page = puller.get_webpage(url)
    soup = bs4.BeautifulSoup(page, features="html.parser")
    return bs4.BeautifulSoup(str(soup.findChildren(class_="feels-like")), features="html.parser").find(class_="temp").contents[0].replace("°", "")


def test():
    print(get_feels_like())
    print(get_temp())


if __name__ == '__main__':
    test()
