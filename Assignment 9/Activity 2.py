def get_score_count(globalAverage):
    print("Average Score is " + str(globalAverage))

def process_average(globalScoreCount, globalTotalScore):
    average = globalTotalScore / globalScoreCount
    
    return average

def get_total_score():
    print("Input Score count")
    inputScoreCount = float(input())
    
    return inputScoreCount

def print_average(globalScoreCount):
    totalScore = 0
    newScoreCount = globalScoreCount
    while newScoreCount > 0:
        print("Input " + str(newScoreCount) + " number of scores" + "Total: " + str(totalScore))
        inputScore = float(input())
        newScoreCount = newScoreCount - 1
        totalScore = totalScore + inputScore
    
    return totalScore

# Main
# A simple program that tells you the average of your scores
globalScoreCount = get_total_score()
globalTotalScore = print_average(globalScoreCount)
globalAverage = process_average(globalScoreCount, globalTotalScore)
get_score_count(globalAverage)
