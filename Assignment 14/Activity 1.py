# A simple program that pulls out text from a file and displays it from high to low


def read_file():
    f = open("scores.txt")
    print(f.read().strip())


def main():
    read_file()


main()
