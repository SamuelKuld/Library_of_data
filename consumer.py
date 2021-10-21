import os
import pickle
import time
import datetime
import fileio.fileio as files
import statistics
import functools
import numpy
import scipy.stats


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
    class no_matching_choice(Exception):
        def __init__(self, message):
            self.message = message
            super().__init__(self.message)

    def print_all_data(data):
        for key in data:
            print(
                f"DateTime : {get_datetime(key)}\nFelt Like : {data[key]['feels-like']}\nActual : {data[key]['temperature']}\n")

    def get_average_difference_of_time(data):
        previous_time = list(data.keys())[0]
        avg_distance_list = []
        for time_ in data:
            avg_distance = (time_ - previous_time) / 2
            previous_time = time_
            avg_distance_list.append(avg_distance)
        return sum(avg_distance_list) / len(avg_distance_list)

    def get_average_temperature(data):
        return statistics.mean([float(temp['temperature'])
                                for temp in [value for key, value in data.items()]])

    def get_average_feeling_temperature(data):
        return statistics.mean([float(temp['feels-like'])
                                for temp in [value for key, value in data.items()]])

    def get_standard_deviation_of_temp(data):
        return statistics.pstdev([float(temp['temperature'])
                                  for temp in [value for key, value in data.items()]])

    def get_standard_deviation_of_feeling(data):
        return statistics.pstdev([float(temp['feels-like'])
                                  for temp in [value for key, value in data.items()]])

    def get_summary_as_string(data):
        return '\n'.join((f"Total Data Points: {len(data)}",
                          f"Timespan : {list(data.keys())[-1] - list(data.keys())[0]}s ",
                          f"  M : or {(list(data.keys())[-1] - list(data.keys())[0])/60}m ",
                          f"  H : or {(list(data.keys())[-1] - list(data.keys())[0])/3600}h.",
                          f"Average Distance of Time (Allows you to see how long it measures temp)= 1 / {get_average_difference_of_time(data)} Seconds",
                          f"  M : or 1 / {get_average_difference_of_time(data) / 60} Minutes",
                          f"Standard Deviation of temperature : {get_standard_deviation_of_temp(data)}",
                          f"Standard Deviation of felt temperature : {get_standard_deviation_of_feeling(data)}",
                          f"Average Temperature : {get_average_temperature(data)}",
                          f"Average Felt Temperature : {get_average_feeling_temperature(data)}",
                          f"Minimum Temperature : {min([value['temperature'] for key, value in data.items()])}",
                          f"Max Temperature : {max([value['temperature'] for key, value in data.items()])}",
                          f"Minimum Felt Temperature : {min([value['feels-like'] for key, value in data.items()])}",
                          f"Max Felt Temperature : {max([value['feels-like'] for key, value in data.items()])}"))  # Finish

    def get_last_24_hours(data):
        day_data = {}
        start_time = time.time()
        for key in list(data.keys())[::-1]:
            """print(key)
            print(time.time())"""
            if start_time - key < 86400:  # 24 hours
                day_data[key] = {
                    "temperature": data[key]["temperature"],
                    "feels-like": data[key]["feels-like"]
                }
            else:
                # Since it's arranged inverted it should automatically
                # sort by greatest to least epoch which means that we can
                # assume if it's greater than 24 hours then it's past the
                # point of necessary iteration.
                break

        day_data = {key: data[key] for key in list(day_data.keys())[::-1]}
        return get_summary_as_string(day_data)

    data = files.read_file("weather.dat", "weather/", type={})
    if data == {}:
        print("No data available or error was raised")
        input()
        return
    choices = ["1", "2", "3", "4", "5", "6", "7", "all"]
    choice = 0

    class Choices():
        def __init__(self):
            self.map_of_choices = {
                "1 ": {"text": " All data points", "func": print_all_data},
                "2 ": {"text": " Average temperature", "func": get_average_temperature},
                "3 ": {"text": " Average felt temperature", "func": get_average_feeling_temperature},
                "4 ": {"text": " Standard deviation of temperature", "func": get_standard_deviation_of_temp},
                "5 ": {"text": " Standard deviation of felt temperature", "func": get_standard_deviation_of_feeling},
                "6 ": {"text": " Get amount of data points", "func": get_summary_as_string},
                "7 ": {"text": " 24 hour summary", "func": get_last_24_hours},
                "all ": {"text": " Prints all data and statistics of data", "func": get_summary_as_string}
            }

        def print_choices(self):
            for key, value in self.map_of_choices.items():
                print(" "*4 + key + ")" + value["text"])

        def run_choice(self, choice, data):
            choice = choice + " "
            if choice not in self.map_of_choices.keys():
                raise no_matching_choice(
                    "There was no matching choice in {self.map_of_choices}")
            return self.map_of_choices[choice]["func"](data)

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
