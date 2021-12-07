# A simple program that prints out addresses for who knows what purpose

def read_file():
    file = open("addresses.txt")
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


def print_function(firstname, lastname, secondfirst, secondlast, thirdfirst, thirdlast, text, firstpost, secondpost, thirdpost):
    print(lastname, ",", firstname, ",", text[1], firstpost[0], ",", firstpost[1], ",", firstpost[2])
    print(secondlast, ",", secondfirst, ",", text[5], secondpost[0], ",", secondpost[1], ",", secondpost[2])
    print(thirdlast, ",", thirdfirst, ",", text[7], thirdpost[0], ",", thirdpost[1], ",", thirdpost[2])


def main():
    text = read_file()
    for index in range(len(text)):
        if index % 4 == 0:
            print(index, text[index].strip())


    # firstname = get_first(text)
    # lastname = get_last(text)
    # firstpost = get_firstpost(text)
    # print_function(firstname, lastname, secondfirst, secondlast, thirdfirst, thirdlast, text, firstpost, secondpost, thirdpost)


main()
