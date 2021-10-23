import bs4
import sys
from puller import *

"""with open("/../web_data/puller.py", "r") as puller:
    data = puller.read()
with open("puller.py", "w+") as file:
    file.write(data)
from puller import *
shutil.remove("puller.py")
"""


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
    results = {}
    table = soup.find('table')
    headers = []
    for header in table.find_all("th"):
        headers.append(header)
    for row in table.find_all("tr"):
        results.append()

    headers = [header.text for header in table.find_all('th')]
    results = [{headers[i]: cell for i, cell in enumerate(row.find_all('td'))}
               for row in table.find_all('tr')]

    print(results)


def test():
    get_crypto_price("dogecoin")


if __name__ == '__main__':
    test()
