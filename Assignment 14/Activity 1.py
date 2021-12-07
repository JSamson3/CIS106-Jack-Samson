# A simple program that pulls out text from a file and displays its average
#
# References:
#   https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/

def read_file():
    file = open("scores.txt")
    text = file.read().replace("\n", ",").split(",")[3::2]
    file.close()
    text = [int(i) for i in text]
    print(text)
    return text


def get_max(text):
    return max(text)
    

def get_min(text):
    return min(text)


def get_average(text):
    output = 0
    for x in text:
        output = output + int(x)
    number = len(text)
    mean = output / number
    return mean


def print_answer(high, low, mean, text):
    print("high", high)
    print("low", low)
    print("mean is", mean)
    print("scores:", text)


def main():
    text = read_file()
    high = get_max(text)
    low = get_min(text)
    mean = get_average(text)
    print_answer(high, low, mean, text)


main()
