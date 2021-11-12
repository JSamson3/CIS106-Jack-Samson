# A program that calculates averages, max, and min


def get_score():
    print("input score")
    newscore = int(input())
    return newscore


def process_inputs():
    scores = []
    while True:
        newscore = get_score()
        if newscore < 0:
            break
        scores.append(newscore)
    return scores


def calculate_max(scores):
    return max(scores)


def calculate_min(scores):
    return min(scores)


def calculate_average(scores):
    output = 0
    for x in scores:
        output = output + x
    number = len(scores)
    average = output / number
    return average


def print_results(high, low, average):
    print("high", high)
    print("low", low)
    print("average is", average)
    

def main():
    scores = process_inputs()

    high = calculate_max(scores)
    low = calculate_min(scores)
    average = calculate_average(scores)
    
    print_results(high, low, average)


main()
