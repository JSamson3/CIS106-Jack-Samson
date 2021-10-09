def input_func1():
    print("Input number")
    input_number = float(input())
    return input_number


def input_func2():
    print("How many times?")
    input_times = float(input())
    return input_times





def the_loop(input_number, input_times):
    number_go_up = 1
    while input_times > 0:


        def processing_func(input_number, input_times, number_go_up):
            print(str(input_number) + " * " + str(number_go_up) + " = " + (str(input_number*number_go_up)))

            
        processing_func(number_go_up, input_times, input_number)
        number_go_up = number_go_up + 1
        input_times = input_times - 1


def main():
    input_number = input_func1()
    input_times = input_func2()
    the_loop(input_number, input_times)


main()