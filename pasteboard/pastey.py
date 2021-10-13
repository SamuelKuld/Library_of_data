import time
import random
import requests


possible_chars = list("abcdefghijklmnopqrstuvwxyz") + \
    list("abcdefghijklmnopqrstuvwxyz".upper())


def generate_url(format=".jpg", previous_code=""):
    if len(previous_code) == 0:
        code = "".join([random.choice(possible_chars) for i in range(12)])
        return ("https://gcdn.pbrd.co/images/" + code + format, code)
    return ("https://gcdn.pbrd.co/images/" + previous_code + format, previous_code)


def get_picture_url(delay=0):
    time.sleep(delay)
    url, code = generate_url()
    result = requests.get(url)
    if result.status_code == 404:
        result = requests.get(generate_url(".png", code)[0])
        if result.status_code == 404:
            return "", code
    elif result.status_code not in [304, 200]:
        print(f"Status code : {result.status_code} ; on : {code}")
        input()
        return "", code

    return url, code


def test():
    start = time.time()
    time.sleep(1)
    url, code = "https://gcdn.pbrd.co/images/" + \
        "r7FCP9vdpPEi" + ".png", "r7FCP9vdpPEi"
    result = requests.get(url)
    if result.status_code == 404:
        result = requests.get(generate_url(".png", code)[0])
        if result.status_code == 404:
            return "", code
    elif result.status_code not in [304, 200]:
        print(f"Status code : {result.status_code} ; on : {url}")
        input()
        url, code = "", code

    url, code = url, code
    print(url)
    print(time.time() - start)


if __name__ == '__main__':
    test()
