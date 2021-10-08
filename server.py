import web_data.puller as puller
import fileio.fileio as files
import random
import os
import statistics
import pickle


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
  """)


def test():
    choice = 0
    possible_choices = ["1", "2"]
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

    clear()


def web_test(url=test_url):
    data_sheet = puller.get_all_elements_in_page(url)
    [print(data.text) for data in data_sheet]
    print("done")


def call():
    test()


if __name__ == '__main__':
    call()
