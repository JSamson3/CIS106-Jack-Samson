# A simple program that multiplies a given number a number of times
number_up = 1


def input_func1():
    print("Input number")
    input_number = int(input())
    return input_number


def input_func2():
    print("How many times?")
    input_times = int(input())
    return input_times


def processing_func(input_number, input_times, number_up):
    output = input_number * number_up
    return output


def the_loop(input_number, input_times):
    number_up = 1
    for output in range(input_times):
        input_times = input_times - 1
        output = processing_func(input_number, input_times, number_up)
        print(str(input_number) + " * " + str(number_up) + " = " + str(output))
        number_up = number_up + 1


def main():
    input_number = input_func1()
    input_times = input_func2()
    the_loop(input_number, input_times)


main()