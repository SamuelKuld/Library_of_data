import os
import bs4
import requests
import socket


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
        soup = bs4.BeautifulSoup(get_webpage(url=url))
    else:
        soup = bs4.BeautifulSoup(webpage)
    results = soup.find(class_=class_)
    if not results:
        raise no_class(f"Could not find {class_} in {url} ")
    else:
        return results


def get_text(class_, url):
    return find_element(class_, url).text


def get_all_elements_in_page(url=test_url, page=""):
    if len(page) == 0:
        data = bs4.BeautifulSoup(get_webpage(url))
    else:
        data = bs4.BeautifulSoup(page)
    sheet = [tag for tag in data.find_all()]
    return sheet
