# A simple program that gives you a multiplication table


def get_number1():
    print("first input?")
    first_input = int(input())
    return first_input


def get_number2():
    print("second input?")
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
    first_input = get_number1()
    second_input = get_number2()
    print_table(first_input, second_input)
    print("end")


main()