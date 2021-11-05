def get_times():
    print("How many times?")
    input_times = int(input())
    return input_times


def process_inputs(input_times):
    scores = []
    for count in range (0 , input_times):
        print(scores)
        print("input number")
        scores.append(int(input()))
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
    print("average is", average)
    

def main():
    input_times = get_times()
    scores = process_inputs(input_times)
    calculate_max(scores)
    calculate_min(scores)
    calculate_average(scores)


main()