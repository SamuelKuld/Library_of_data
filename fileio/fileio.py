import shutil
import os
import pickle
import sys

# Need to do this in order to save and read the weather data loop.
sys.setrecursionlimit(3000)


def find_file(name="untitled.txt", directory=os.getcwd()):
    file_info = {}
    file_info['name'] = name
    if name in os.listdir(directory):
        file_info['in_current_directory'] = True
    if len(name.split(".")) == 0:
        file_info['is_file_directory'] = True
    file_info['type'] = name.split(".")[-1]
    return file_info


def is_file_in_directory(name="untitled.txt", directory=os.getcwd()):
    if name in os.listdir(directory):
        return True
    return False


def is_file_name_in_directory(name="untitled.txt", directory=os.getcwd()):
    if name in [i.split('.')[0] for i in os.listdir(directory)]:
        return True
    return False


def create_directory(name, directory=os.getcwd()):
    if name in os.listdir(directory):
        shutil.rmtree(name)
        os.mkdir(name)
    else:
        print("False")
        os.mkdir(name)


def create_file(name, directory=os.getcwd(), contents=""):
    if "\\" != directory[-2::] and "/" != directory[-1]:
        if type(contents) == type(""):
            with open(directory + "\\" + name, "w+") as file:
                file.write(contents)
        else:
            with open(directory + "\\" + name, "wb+") as file:
                pickle.dump(contents, file)
                return
    elif "/" != directory[-1::]:
        if type(contents) == type(""):
            with open(directory + "/" + name, "w+") as file:
                file.write(contents)
        else:
            with open(directory + "/" + name, "wb+") as file:
                pickle.dump(contents, file)
    else:
        if type(contents) == type(""):
            with open(directory + name, "w+") as file:
                file.write(contents)
        else:
            with open(directory + name, "wb+") as file:
                pickle.dump(contents, file)


def read_file(name, directory=os.getcwd(), type={}):
    try:
        if "\\" != directory[-2::] and "/" != directory[-1]:
            with open(directory+"\\" + name, "rb") as file:
                data = pickle.load(file)
            return data
        elif "/" != directory[-1::]:
            with open(directory+"/" + name, "rb") as file:
                data = pickle.load(file)
            return data
        else:
            with open(directory + name, "rb") as file:
                data = pickle.load(file)
            return data
    except:
        return type


class File():
    def __init__(self, name="untitled.txt", directory=os.getcwd()):
        self.name = name
        self.directory = directory

    def find_file(self):
        return find_file(self.name, self.directory)

    def is_file_name_in_directory(self):
        return is_file_name_in_directory(self.name, self.directory)

    def is_file_in_directory(self):
        return is_file_in_directory(self.name, self.directory)
