# A simple program that prints out addresses for who knows what purpose

def read_file():
    file = open("addresses.txt")
    text = file.readlines()
    file.close()
    return text


def main():
    text = read_file()
    for index in range(len(text)):
        if index % 4 == 0:
            print(text[index].strip().split(" ")[1], text[index].strip().split(" ")[0], sep=", ", end=", ")
        if index % 4 == 1:
            print(text[index].strip(), sep=", ", end=", ")
        if index % 4 == 2:
            print(text[index].strip(), sep=", ", end="\n")


main()
