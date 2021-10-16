# A simple program that multiplies a given number a number of times


def get_number():
    print("Input number")
    input_number = int(input())
    return input_number


def get_times():
    print("How many times?")
    input_times = int(input())
    return input_times


def calculate_product(input_number, count):
    output = input_number * count
    return output


def display_expression(input_number, count, output):
    print(str(input_number) + " * " + str(count) + " = " + str(output))


def process_expressions(input_number, input_times):
    for count in range(1, input_times + 1):
        output = calculate_product(input_number, count)
        display_expression(input_number, count, output)


def main():
    input_number = get_number()
    input_times = get_times()
    process_expressions(input_number, input_times)


main()
