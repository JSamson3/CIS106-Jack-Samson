def get_score_count(Average):
    print("Average Score is " + str(Average))

def process_average(ScoreCount, TotalScore):
    average = TotalScore / ScoreCount
    
    return average

def get_total_score():
    print("Input Score count")
    inputScoreCount = float(input())
    
    return inputScoreCount

def print_average(ScoreCount):
    totalScore = 0
    newScoreCount = ScoreCount
    while newScoreCount > 0:
        print("Input " + str(newScoreCount) + " number of scores" + "Total: " + str(totalScore))
        inputScore = float(input())
        newScoreCount = newScoreCount - 1
        totalScore = totalScore + inputScore
    
    return totalScore

# Main
# A simple program that tells you the average of your scores
ScoreCount = get_total_score()
TotalScore = print_average(ScoreCount)
Average = process_average(ScoreCount, TotalScore)
get_score_count(Average)
