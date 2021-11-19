# A simple program that asks for your name


def get_name():
    print("Input first then last name")
    userinput = input(str())
    if userinput.find(" ") == -1:
        while userinput.find(" ") == -1:
            print("input a valid name")
            userinput = input(str())
        return userinput
    else:
        return userinput


def split_name(userinput):
    userinput = userinput.split()
    return userinput


def split_first(userinput):
    firstname = userinput[0]
    return firstname


def split_last(userinput):
    lastname = userinput[1]
    return lastname


def print_name(firstname, lastname):
    print(lastname + ", " + firstname[0] + ".")


def main():
    userinput = get_name()
    userinput = split_name(userinput)
    firstname = split_first(userinput)
    lastname = split_last(userinput)
    print_name(firstname, lastname)


main()
