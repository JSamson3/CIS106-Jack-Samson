# A simple program that prints out addresses for who knows what purpose

def read_file():
    file = open("Addresses.txt")
    text = file.readlines()
    file.close()
    return text


def get_first(text):
    firstname = text[0].split(" ")[0]
    return firstname


def get_last(text):
    lastname = text[0].split(" ")[1]
    return lastname
    

def get_firstpost(text):
    firstpost = text[2].split(" ")
    return firstpost


def main():
    text = read_file()
    for index in range(len(text)):
        if index % 4 == 0:
            print(text[index].strip().split(" ")[1], text[index].strip().split(" ")[0], sep=", ", end=", ")
        if index % 4 == 1:
            print(text[index].strip(), sep=", ", end=", ")
        if index % 4 == 2:
            print(text[index].strip(), sep=", ", end=", ")
        if index % 4 == 4:
            print(index, text[index].strip(), sep=", ", end="\n")

    # firstname = get_first(text)
    # lastname = get_last(text)
    # firstpost = get_firstpost(text)
    # print_function(firstname, lastname, secondfirst, secondlast, thirdfirst, thirdlast, text, firstpost, secondpost, thirdpost)


main()
