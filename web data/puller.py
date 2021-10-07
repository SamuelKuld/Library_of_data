import os
import bs4
import requests
import socket


def ping(url="https://www.york.ac.uk/teaching/cws/wws/webpage1.html"):
    socket_engine = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        socket_engine.connect(url)
        return True
    except:
        return False


def get_webpage(url="https://www.york.ac.uk/teaching/cws/wws/webpage1.html"):
    if ping(url):
        return requests.get(url, headers={"user-agent": "google.com"}).text
    else:
        raise Exception(
            f"URL (\"{url}\") was unable to connect. Please try different URL")
