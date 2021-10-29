# A simple program that gives you a multiplication table


def get_starting():
    print("starting?")
    starting_input = int(input())
    return starting_input


def get_ending():
    print("ending?")
    ending_input = int(input())
    return ending_input


def print_table(starting_input, ending_input):
    print((" "), end=" ")
    for c in range(starting_input, ending_input + 1):
        print((c), end=" ")
    print()
    for a in range(starting_input, ending_input + 1):
        print((a), end=" ")
        for b in range(starting_input, ending_input + 1):
            print((a * b), end=" ")
        print()


def main():
    starting_input = get_starting()
    ending_input = get_ending()
    print_table(starting_input, ending_input)


main()