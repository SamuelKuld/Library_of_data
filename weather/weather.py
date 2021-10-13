# Puller functions, can't do this any other way.
import bs4
import requests


test_url = "https://www.york.ac.uk/teaching/cws/wws/webpage1.html"


class no_connection(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class no_class(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def ping(url=test_url):
    return True


def get_webpage(url=test_url):
    if ping(url):
        return requests.get(url, headers={"user-agent": "google.com"}).text
    else:
        raise no_connection(
            f"URL (\"{url}\") was unable to connect. Please try different URL")


def find_element(class_, url=test_url, webpage=""):
    if len(webpage) == 0:
        soup = bs4.BeautifulSoup(get_webpage(url=url), features="html.parser")
    else:
        soup = bs4.BeautifulSoup(webpage, features="html.parser")
    results = soup.find(class_=class_)
    if not results:
        raise no_class(f"Could not find {class_} in {url} ")
    else:
        return results


def get_text(class_, url):
    return find_element(class_, url).text


def get_all_elements_in_page(url=test_url, page=""):
    if len(page) == 0:
        data = bs4.BeautifulSoup(get_webpage(url), features="html.parser")
    else:
        data = bs4.BeautifulSoup(page, features="html.parser")
    sheet = [tag for tag in data.find_all()]
    return sheet


weather_url = "https://www.wunderground.com/weather/us/ca/alturas"
temperature_element = "wu-value wu-value-to"
feels_like_element = ""
# Test


def get_temp(url=weather_url, page=""):
    if not bool(page):
        page = get_webpage(url)
    return str(find_element(temperature_element, webpage=page).contents[0])


def get_feels_like(url=weather_url, page=""):
    if not page:
        page = get_webpage(url)
    soup = bs4.BeautifulSoup(page, features="html.parser")
    return str(bs4.BeautifulSoup(str(soup.findChildren(class_="feels-like")), features="html.parser").find(class_="temp").contents[0].replace("°", ""))


def test():
    print(get_feels_like())
    print(get_temp())


if __name__ == '__main__':
    test()
