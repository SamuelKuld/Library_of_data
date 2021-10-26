import os
import pickle
import time
import datetime
import fileio.fileio as files
from weather.weahter_functs import *


def clear():
    os.system("cls")


def get_datetime(epoch_time=time.time()):
    date_time = datetime.datetime.fromtimestamp(epoch_time)
    return date_time.strftime("%m - %d - %Y - %H:%M:%S")


def input(prompt='>>> ', input_funct=input):
    return input_funct(prompt)


def get_numerical_data(name):
    if not files.is_file_name_in_directory(name):
        return ""
    if files.is_file_name_in_directory(name, name):
        with open(name + "\\" + name + "_info.dat", "rb") as file:
            contents = pickle.load(file)
        return contents


def test():
    if not files.is_file_name_in_directory("test"):
        print("Data hasn't been collected, please run server first.")
        input()
        return
    else:
        data = get_numerical_data("test")
        print(
            f"mean : {data['mean']}",
            f"median : {data['median']}",
            f"standard deviation : {data['standard_deviation']}",
            sep="\n")
        input()


def get_images():
    print("Grabbing all current images")
    if not files.is_file_name_in_directory("images"):
        print("There are no images. Please run the images function in the server module.")
        input()
        pass
    else:
        print("Showing images")
        os.system("start images/images.html")
        print("Done.")
        input()


def get_weather():

    data = files.read_file("weather.dat", "weather/", type={})
    if data == {}:
        print("No data available or error was raised")
        input()
        return
    choices = ["1", "2", "3", "4", "5", "6", "7", "all"]
    choice = 0

    while choice != "exit":
        choices = Choices()
        always_run = 1
        choice = 0
        while choice != "exit":
            try:
                while always_run == 1:
                    print("What would you like to see?")
                    choices.print_choices()
                    choice = input()
                    if choice == "exit":
                        break
                    data = files.read_file("weather.dat", "weather/", type={})
                    clear()
                    result = choices.run_choice(choice, data)
                    if result == None:
                        continue
                    print(result)
                    input()
                    clear()
            except no_matching_choice:
                print("Please choose a valid choice")

        clear()
    print("Done.")
    clear()
    pass


def main():
    def print_choices():
        print("""
        1 ) Test
        2 ) Get Images
        3 ) Get Weather Data
        """)

    possible_choices = ["1", "2", "3"]
    choice = 0
    while choice not in possible_choices:
        clear()
        print("Choices:")
        print_choices()
        choice = input()
    clear()
    if choice == "1":
        test()
    elif choice == "2":
        get_images()
    elif choice == "3":
        get_weather()


if __name__ == "__main__":
    main()
