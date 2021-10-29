def get_number1():
    print("input 1")
    input1 = int(input())
    return input1


def get_number2():
    print("input 2")
    input2 = int(input())
    return input2


def print_table(input1, input2):
    for i in range(1, input1 + 1):
        for j in range(1, input2 + 1):
            print((i * j), end = " ")
        print()


def main():
    input1 = get_number1()
    input2 = get_number2()
    print_table(input1, input2)


main()