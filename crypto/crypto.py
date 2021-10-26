import bs4
import sys
from puller import *


def get_crypto_link(name):
    return "https://coinmarketcap.com/currencies/" + name + "/"


def get_crypto_list(list_of_cryptos):
    return [get_crypto_link(name) for name in list_of_cryptos]


def get_crypto_page(crypto):
    return get_webpage(get_crypto_link(crypto))


def get_crypto_webpage_list(list_of_cryptos):
    return [get_webpage(get_crypto_link(crypto)) for crypto in list_of_cryptos]


def get_crypto_price(crypto):
    page = get_crypto_page(crypto)
    soup = bs4.BeautifulSoup(page, features="html.parser")
    price = soup.find(class_="priceValue").text.replace("$", "")
    return float(price)


def test():
    print(get_crypto_price("dogecoin"))


if __name__ == '__main__':
    test()
