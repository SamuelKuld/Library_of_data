import os
import shutil


with open(os.path.dirname(__file__) + "/../web_data/puller.py", "r") as puller:
    data = puller.read()
with open("puller.py", "w+") as file:
    file.write(data)
from puller import *
os.remove("puller.py")


def get_crypto_link(name):
    return "https://coinmarketcap.com/currencies/" + name + "/"


def get_crypto_list(list_of_cryptos):
    return [get_crypto_link(name) for name in list_of_cryptos]


def get_crypto_page(crypto):
    return get_webpage(get_crypto_link(crypto))


def get_crypto_webpage_list(list_of_cryptos):
    return [get_webpage(get_crypto_link(crypto)) for crypto in list_of_cryptos]
