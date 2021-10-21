# A simple program that multiplies a given number a number of times


def get_number():
    print("Input number")
    input_number = int(input())
    return input_number


def get_times():
    print("How many times?")
    input_times = int(input())
    return input_times


def calculate_number(input_number, input_times, number_up):
    output = input_number * number_up
    return output


def process_expressions(input_number, input_times):
    number_up = 1
    while input_times > 0:
        input_times = input_times - 1
        output = calculate_number(input_number, input_times, number_up)
        print(str(input_number) + " * " + str(number_up) + " = " + str(output))
        number_up = number_up + 1


def main():
    input_number = get_number()
    input_times = get_times()
    process_expressions(input_number, input_times)


main()