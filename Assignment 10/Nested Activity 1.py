# A simple program that gives you a multiplication table


def get_number1():
    print("FirstInput?")
    FirstInput = int(input())
    return FirstInput


def get_number2():
    print("second?")
    SecondInput = int(input())
    return SecondInput


def print_table(FirstInput, SecondInput):
    print((" "), end=" ")
    for c in range(FirstInput, SecondInput + 1):
        print((c),end=" ")
    print()
    for a in range(FirstInput, SecondInput + 1):
        print((a), end=" ")
        for b in range(FirstInput, SecondInput + 1):
            print((a * b), end=" ")
        print()


def main():
    FirstInput = get_number1()
    SecondInput = get_number2()
    print_table(FirstInput, SecondInput)
    print("end")


main()