import os
import pickle
import fileio.fileio as files


def clear():
    os.system("cls")


def print_choices():
    print("""
    1 ) Test
    2 ) Get Images
    """)


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


def main():
    possible_choices = ["1", "2"]
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


if __name__ == "__main__":
    main()
