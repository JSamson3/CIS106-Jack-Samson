# A program that calculates averages, max, and min


def process_inputs():
    scores = []
    newscore = 1
    while newscore > -1:
        print(scores)
        print("input score")
        newscore = int(input())
        if newscore < 0:
            break
        scores.append(newscore)
        scores.sort()
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
    scores = process_inputs()

    calculate_max(scores)
    calculate_min(scores)
    average = calculate_average(scores)
    
    print_average(average)


main()
