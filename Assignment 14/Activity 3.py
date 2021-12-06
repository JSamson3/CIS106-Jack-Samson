# Fuck you


def input_function():
    print("input")
    name = str(input())
    if name.find(".html") == -1: 
        while name.find(".html") == -1:
            print("input valid name")
            name = str(input())
        return name
    if name.find(".txt") == -1:
        while name.find(".txt") == -1:
            print("input valid name")
            name = str(input())
    else:
        return name


def open_file(name):
    open(name , "at")
