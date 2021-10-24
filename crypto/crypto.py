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
    table = soup.find('table')
    results = [[cell for i, cell in enumerate(row.find_all('td'))]
               for row in table.find_all('tr')]  # Going to analyze this later because I am not entirely sure how it works
    results = [i[0] for i in results]
    print(results[0].text.replace("$", ""))
    input()


def test():
    get_crypto_price("dogecoin")


if __name__ == '__main__':
    test()
