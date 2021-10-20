import web_data.puller as puller
import fileio.fileio as files
import pasteboard.pastey as pastey
import weather.weather as weather
import time
import random
import os
import pprint
import statistics


test_url = "https://www.york.ac.uk/teaching/cws/wws/webpage1.html"


def input(prompt='>>> ', input_funct=input):
    return input_funct(prompt)


def clear():
    os.system("cls")


def create_simple_numbers(file_name="untitled", list_of_values=[random.randint(0, 100) for i in range(1000)]):
    files.create_directory(file_name)
    files.create_file(file_name + ".txt", file_name,
                      contents="\n".join([str(i) for i in list_of_values]))
    files.create_file(file_name + "_info.dat",
                      file_name,
                      contents={"mean": statistics.mean(list_of_values),
                                "median": statistics.median(list_of_values),
                                "standard_deviation": statistics.stdev(list_of_values), })


def print_choices():
    print("""
  1 ) Test
  2 ) Web Test
  3 ) Get Images
  4 ) Get Weather Data
  """)


def web_test(url=test_url):
    data_sheet = puller.get_all_elements_in_page(url)
    [print(data.text) for data in data_sheet]
    print("done")


def get_images():
    while True:
        url, code = pastey.get_picture_url(delay=1)
        if url == "":
            print(f"[ERROR] url : {code} does not exist")
            continue
        if not files.is_file_name_in_directory("images"):
            files.create_directory("images")
        with open("images/images.html", "a+") as file:
            print(url)
            file.write(f"<img src={url}></img>\n")


def weather_data_loop():
    if not files.is_file_in_directory(name='weather.dat', directory='weather/'):
        files.create_file("weather.dat", 'weather/', contents={})
    data = files.read_file("weather.dat", directory='weather/')
    while True:
        start = time.time()
        weather_page = weather.get_weather()
        temperature = weather.get_temp(page=weather_page)
        felt_like = weather.get_feels_like(page=weather_page)

        # Apparently sometimes the webpage doesn't calculate it?
        # This basically allows us to skip over invalid data points and stat from the beginning, skipping the timer.
        if felt_like == "--":
            continue
        elif temperature == "--":
            continue
        data[time.time()] = {"temperature": temperature,
                             "feels-like": felt_like}
        files.create_file('weather.dat', 'weather/', data)
        # pprint.pprint(data, indent=2, depth=3)
        print(len(data))
        time.sleep(60 - (time.time() - start))


def weather_cleaner():
    proper_weather = {}
    data = files.read_file("weather.dat", "weather/")
    for key, value in data.items():
        print(value)
        if "--" not in value["feels-like"]:
            proper_weather[key] = value
        elif "--" not in value["temperature"]:
            proper_weather[key] = value
        else:
            print(key, value, sep=" ")
            input()
            continue
    files.create_file("weather.dat", "weather/", proper_weather)


def test():
    choice = 0
    possible_choices = ["1", "2", "3", "4", "5"]
    while choice not in possible_choices:
        print("What would you like to do?")
        print_choices()
        choice = input()
        clear()
    if choice == "1":
        create_simple_numbers("test", list_of_values=[
                              random.randint(0, 100) for i in range(1000)])
        print("Done")
    elif choice == "2":
        web_test()
    elif choice == "3":
        get_images()
    elif choice == "4":
        weather_data_loop()
    elif choice == "5":
        weather_cleaner()

    clear()


def call():
    test()


if __name__ == '__main__':
    call()
