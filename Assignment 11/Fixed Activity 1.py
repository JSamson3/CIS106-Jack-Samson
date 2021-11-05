# A program that calculates averages, max, and min
def get_times():
    print("How many times?")
    input_times = int(input())
    return input_times


def process_inputs(input_times):
    scores = [None] * input_times
    for count in range(0, input_times):
        print(scores)
        print("input score")
        scores[count] = (int(input()))
    print(scores)
    return scores


def calculate_max(scores):
    print("high", max(scores))


def calculate_min(scores):
    print("low", min(scores))


def calculate_average(scores):
    output = 0
    for x in scores:
        output = output + x
    number = len(scores)
    average = output / number
    return average


def print_average(average):
    print("average is", average)
    

def main():
    input_times = get_times()
    scores = process_inputs(input_times)
    calculate_max(scores)
    calculate_min(scores)
    average = calculate_average(scores)
    print_average(average)


main()