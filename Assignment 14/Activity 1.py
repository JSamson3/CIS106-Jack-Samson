# A simple program that pulls out text from a file and displays its average


def read_file():
    text = open("Assignment 14\scores.txt")
    file = text.read().replace("\n", ",").split(",")[3::2]
    text.close()
    print(file)
    return file


def get_max(file):
    int("".join(str(i) for i in file))
    return max(file)
    

def get_min(file):
    return min(file)


def get_average(file):
    output = 0
    for x in file:
        output = output + int(x)
    number = len(file)
    mean = output / number
    return mean


def print_answer(high, low, mean, file):
    print("high", high)
    print("low", low)
    print("mean is", mean)
    print("scores:", file)


def main():
    file = read_file()
    high = get_max(file)
    low = get_min(file)
    mean = get_average(file)
    print_answer(high, low, mean, file)


main()
