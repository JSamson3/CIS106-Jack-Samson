# A simple program that pulls out text from a file and displays it from high to low


from os import read


def read_file():
    f = open("Assignment 14\scores.txt")
    print(f.read().strip())


def main():
    read_file()


main()