import statistics
import datetime
import time
import fileio.fileio as files


def get_datetime(epoch_time=time.time()):
    date_time = datetime.datetime.fromtimestamp(epoch_time)
    return date_time.strftime("%m - %d - %Y - %H:%M:%S")


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


def get_data_without_zero(data, key_):
    data_without_zero = []
    for key, value in data.items():
        if value[key_] != "0":
            data_without_zero.append(float(value[key_]))
        else:
            continue
    return data_without_zero


def get_type(type, data):
    new_data = {}
    for key, value in data.items():
        if type not in list(value.keys()):
            continue
        new_data[key] = value
    return new_data


def get_summary_as_string(data):
    temperatures = get_type("temperature", data)
    felt_temperatures = get_type("feels-like", data)

    return '\n'.join((f"Total Data Points: {len(data)}",
                      f"Timespan : {list(data.keys())[-1] - list(data.keys())[0]}s ",
                      f"  M : or {(list(data.keys())[-1] - list(data.keys())[0])/60}m ",
                      f"  H : or {(list(data.keys())[-1] - list(data.keys())[0])/3600}h.",
                      f"Average Distance of Time (Allows you to see how long it measures temp)= 1 / {get_average_difference_of_time(data)} Seconds",
                      f"  M : or 1 / {get_average_difference_of_time(data) / 60} Minutes",
                      f"Standard Deviation of temperature : {get_standard_deviation_of_temp(temperatures)}",
                      f"Standard Deviation of felt temperature : {get_standard_deviation_of_feeling(felt_temperatures)}",
                      f"Average Temperature : {get_average_temperature(temperatures)}",
                      f"Average Felt Temperature : {get_average_feeling_temperature(felt_temperatures)}",
                      f"Minimum Temperature : {min(get_data_without_zero(temperatures, 'temperature'))}",
                      f"Max Temperature : {max([value['temperature'] for key, value in temperatures.items()])}",
                      f"Minimum Felt Temperature : {min(get_data_without_zero(felt_temperatures, 'feels-like'))}",
                      f"Max Felt Temperature : {max([value['feels-like'] for key, value in get_type('feels-like',data).items()])}"))  # Finish


def get_last_24_hours(data):
    day_data = {}
    start_time = time.time()
    for key in list(data.keys())[::-1]:
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

    day_data = {key: value for key, value in list(day_data.items())[::-1]}
    return get_summary_as_string(day_data)


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
