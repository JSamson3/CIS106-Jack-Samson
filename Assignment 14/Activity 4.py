# A simple program that prints out addresses for who knows what purpose

def read_file():
    file = open("addresses.txt")
    new = file.readlines()
    file.close()
    return new


def output_function(new):
    for index in range(len(new)):
        if index < 4:
            if index % 4 == 0:
                print(new[index].strip().split()[1], end=", ")
                print(new[index].strip().split()[0], sep=", ", end=", ")
            if index % 4 == 1:
                print(new[index].strip(), sep=", ", end=", ")
            if index % 4 == 2:
                print(new[index].strip().split(",")[0], sep=", ", end=", ")
                print(new[index].replace(" ", ", ").split(", ")[1], end=", ")
                print(new[index].replace(" ", ", ").split(", ")[2], end="")
        if index >= 4:
            if index % 4 == 0:
                print(new[index].strip().split()[1], end=", ")
                print(new[index].strip().split()[0], sep=", ", end=", ")
            if index % 4 == 1:
                print(new[index].strip(), sep=", ", end=", ")
            if index % 4 == 2:
                print(new[index].strip().split(",")[0], sep=", ", end=", ")
                print(new[index].replace(", ", " ").split()[2], end=", ")
                print(new[index].replace(",", " ").split()[3], end="\n")


def main():
    new = read_file()
    output_function(new)


main()
