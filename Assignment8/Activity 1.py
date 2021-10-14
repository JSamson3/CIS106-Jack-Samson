#A simple program that multiplies a given number a number of times
number_go_up = 1


def input_func1():
    print("Input number")
    input_number = int(input())
    return input_number


def input_func2():
    print("How many times?")
    input_times = int(input())
    return input_times


def processing_func(input_number, input_times, number_go_up):
    new_print = input_number * number_go_up
    return new_print


def the_loop(input_number, input_times):
    number_go_up = 1
    while input_times > 0:
        input_times = input_times - 1
        new_print = processing_func(input_number, input_times, number_go_up)
        print(str(input_number) + " * " + str(number_go_up) + " = " + str(new_print))
        number_go_up = number_go_up + 1



def main():
    input_number = input_func1()
    input_times = input_func2()
    the_loop(input_number, input_times)


main()