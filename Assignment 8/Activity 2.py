# A simple program that tells you the average of your scores


def get_score_count():
    print("Input total score count")
    inputScoreCount = int(input())    
    return inputScoreCount


def get_score(count, total_score):
        print("Input " + str(count) + " scores. " + "Total: " + str(total_score))
        input_score = float(input())
        return input_score


def get_total_score(score_count):
    total_score = 0
    for count in range(score_count, 0, -1):
        input_score = get_score(count, total_score)
        total_score = total_score + input_score
    
    return total_score


def process_average(ScoreCount, TotalScore):
    average = TotalScore / ScoreCount    
    return average


def display_average(Average):
    print("Average Score is " + str(Average))


def main():
    score_count = get_score_count()
    total_score = get_total_score(score_count)
    average = process_average(score_count, total_score)
    display_average(average)


main()
