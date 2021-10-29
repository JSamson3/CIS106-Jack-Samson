# A simple program that gives you a multiplication table


def get_starting():
    print("starting?")
    first_input = int(input())
    return first_input


def get_ending():
    print("ending?")
    second_input = int(input())
    return second_input


def print_table(first_input, second_input):
    print((" "), end=" ")
    for c in range(first_input, second_input + 1):
        print((c), end=" ")
    print()
    for a in range(first_input, second_input + 1):
        print((a), end=" ")
        for b in range(first_input, second_input + 1):
            print((a * b), end=" ")
        print()


def main():
    first_input = get_starting()
    second_input = get_ending()
    print_table(first_input, second_input)


main()