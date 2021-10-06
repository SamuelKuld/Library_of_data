import fileio.fileio as files
import random
import os
import statistics
import pickle


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
  2 ) Test 2
  """)


def test():
    choice = 0
    possible_choices = ["1"]
    while choice not in possible_choices:
        print("What would you like to do?")
        print_choices()
        choice = input()
        clear()
    if choice == "1":
        create_simple_numbers("test", list_of_values=[
                              random.randint(0, 100) for i in range(1000)])
        print("Done")

    clear()


def call():
    test()


if __name__ == '__main__':
    call()
