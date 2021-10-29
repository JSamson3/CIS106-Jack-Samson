# A simple program that gives you a multiplication table


def get_number1():
    print("first?")
    input1 = int(input())
    return input1


def get_number2():
    print("second?")
    input2 = int(input())
    return input2


def print_table(input1, input2):
    print((""), end = "")
    for a in range(input1, input2 + 1):
        print((a), end = " ")
        for b in range(input1, input2 + 1):
            print((a * b), end=" ")
        print()


def main():
    input1 = get_number1()
    input2 = get_number2()
    print_table(input1, input2)
    print("end")


main()