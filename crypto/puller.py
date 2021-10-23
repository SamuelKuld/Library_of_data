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
        return requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.73"}).text
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
