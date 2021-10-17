import os
import pickle
import time
import datetime
import fileio.fileio as files
import statistics
import functools


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

    def get_average_temperature(data):
        return statistics.mean([float(temp['temperature'])
                                for temp in [value for key, value in data.items()]])

    def get_average_feeling_temperature(data):
        return statistics.mean([float(temp['feels-like'])
                                for temp in [value for key, value in data.items()]])

    def get_standard_deviation_of_temp(data):
        return statistics.stdev([float(temp['temperature'])
                                for temp in [value for key, value in data.items()]])

    def get_standard_deviation_of_feeling(data):
        return statistics.stdev([float(temp['feels-like'])
                                for temp in [value for key, value in data.items()]])

    data = files.read_file("weather.dat", "weather/", type={})
    if data == {}:
        print("No data available or error was raised")
        input()
        return
    choices = ["1", "2", "3", "4", "5", "6", "all"]
    choice = 0
    while choice != "exit":
        print("What would you like to see?")
        print("""
              1 ) All data points
              2 ) Average temperature
              3 ) Average feeling temperature
              4 ) Standard deviation of temperature
              5 ) Standard deviation of feeling temperature
              6 ) Get amount of data points
              all ) Prints all data and statistics of data
              """)
        choice = input()
        clear()
        if choice == "1":
            for key in data:
                print(
                    f"DateTime : {get_datetime(key)}\nFelt Like : {data[key]['feels-like']}\nActual : {data[key]['temperature']}\n")
        elif choice == "2":
            print(f"Average Temperature : {get_average_temperature(data)}")
        elif choice == "3":
            print(
                f"Average felt temperature : {get_average_feeling_temperature(data)}")
        elif choice == "4":
            print(
                f"Standard deviation of temperature : {get_standard_deviation_of_temp(data)}")
        elif choice == "5":
            print(
                f"Standard Deviation of Felt temperature : {get_standard_deviation_of_feeling(data)}")
        elif choice == "6":
            print(
                f"Total Data Points: {len(data)}",
                f"Timespan : {list(data.keys())[-1] - list(data.keys())[0]}s ",
                f"or {(list(data.keys())[-1] - list(data.keys())[0])/60}m ",
                f"or {(list(data.keys())[-1] - list(data.keys())[0])/3200}h.",
                f"Standard Deviation of Time (Allows you to see how long it measures temp)= 1 / {statistics.stdev([key for key in data.keys()])} Seconds",
                f"Or 1 / {statistics.stdev([key for key in data.keys()]) / 60} Minutes", sep="\n")
        elif choice.lower() == "all":
            for key, value in data.items():
                print(
                    f"DateTime : {get_datetime(key)}\nFelt Like : {value['feels-like']}\nActual : {value['temperature']}\n")
            print(f"Average Temperature : {get_average_temperature(data)}")
            print(
                f"Average Feels like : {get_average_feeling_temperature(data)}")
            print(
                f"Standard Deviation of temp : {get_standard_deviation_of_temp(data)}")
            print(
                f"Standard Deviation of feeling : {get_standard_deviation_of_feeling(data)}")
            print(
                f"Total Data Points: {len(data)}",
                f"Timespan : {list(data.keys())[-1] - list(data.keys())[0]}s ",
                f"or {(list(data.keys())[-1] - list(data.keys())[0])/60}m ",
                f"or {(list(data.keys())[-1] - list(data.keys())[0])/3200}h.",
                f"Standard Deviation of Time (Allows you to see how long it measures temp)= 1 / {statistics.stdev([key for key in data.keys()])} Seconds",
                f"Or 1 / {statistics.stdev([key for key in data.keys()]) / 60} Minutes", sep="\n")
        elif choice == "exit":
            break
        input()
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
