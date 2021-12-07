# A simple program that prints out addresses for who knows what purpose


from os import close


def create_func():
    try:
        f = open("thing.txt")
        text = f.read.splitlines()
        f.close()
        return text
    except:
        f = open("thing.txt", "x")
        f.write("Firstname Lastname\n123 Any Street\nCity, State/Province/Region PostalCode\n1stname 2ndname\n123 Any Street\nCity, State/Province/Region PostalCode\n3rdname 4thname\n123 Any Street\nCity, State/Province/Region PostalCode")
        f.close()
        f = open("thing.txt")
        text = f.read().splitlines()
        f.close()
        return text


def get_first(text):
    firstname = text[0].split(" ")[0]
    return firstname


def get_last(text):
    lastname = text[0].split(" ")[1]
    return lastname
    

def get_secondfirst(text):
    secondfirst = text[3].split(" ")[0]
    return secondfirst


def get_secondlast(text):
    secondlast = text[3].split(" ")[1]
    return secondlast


def get_thirdfirst(text):
    thirdfirst = text[6].split(" ")[0]
    return thirdfirst


def get_thirdlast(text):
    thirdlast = text[6].split(" ")[1]
    return thirdlast


def get_firstpost(text):
    firstpost = text[2].split(" ")
    return firstpost


def get_secondpost(text):
    secondpost = text[5].split(" ")
    return secondpost


def get_thirdpost(text):
    thirdpost = text[8].split(" ")
    return thirdpost


def print_function(firstname, lastname, secondfirst, secondlast, thirdfirst, thirdlast, text, firstpost, secondpost, thirdpost):
    print(lastname, ",", firstname, ",", text[1], firstpost[0], ",", firstpost[1], ",", firstpost[2])
    print(secondlast, ",", secondfirst, ",", text[5], secondpost[0], ",", secondpost[1], ",", secondpost[2])
    print(thirdlast, ",", thirdfirst, ",", text[7], thirdpost[0], ",", thirdpost[1], ",", thirdpost[2])


def main():
    text = create_func()
    firstname = get_first(text)
    lastname = get_last(text)
    secondfirst = get_secondfirst(text)
    secondlast = get_secondlast(text)
    thirdfirst = get_thirdfirst(text)
    thirdlast = get_thirdlast(text)
    firstpost = get_firstpost(text)
    secondpost = get_secondpost(text)
    thirdpost = get_thirdpost(text)
    print_function(firstname, lastname, secondfirst, secondlast, thirdfirst, thirdlast, text, firstpost, secondpost, thirdpost)


main()