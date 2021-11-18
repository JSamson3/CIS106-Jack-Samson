# A simple program that reverses the line of text that you give it


def get_input():
    print("input a line of text")
    userinput = input(str())
    return userinput


def split_string(userinput):
    single_spaces = " ".join(userinput.split())
    return single_spaces


def reverse_print(single_spaces):
    print(single_spaces[::-1])


def main():
    userinput = get_input()
    single_spaces = split_string(userinput)
    reverse_print(single_spaces)


main()