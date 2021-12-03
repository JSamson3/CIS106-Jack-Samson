# A simple program that pulls out text from a file and displays it from high to low


from os import read


def read_file():
    f = open("Assignment 14\scores.txt")
    file = f.read().replace("\n", ",").split(",")
    f.close()
    print(file)
    return file


def get_max(file):
    return max(file)
    

def get_min(file):
    return min(file)


def get_average(file):
    output = 0
    for x in file:
        output = output + x
    number = len(file)
    average = output / ((number - 2 ) / 2)
    return average


def print_answer(average, low, high, file):
    print("high", high)
    print("low", low)
    print("average is", average)
    print("scores:", file)



def main():
    file = read_file()
    high = get_max(file)
    low = get_min(file)
    average = get_average(file)
    print_answer(high, low, average, file)



main()