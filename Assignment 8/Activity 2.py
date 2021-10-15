def averageFunc(globalAverage):
    print("Average Score is " + str(globalAverage))

def averageProcessing(globalScoreCount, globalTotalScore):
    average = globalTotalScore / globalScoreCount
    
    return average

def inputFunc():
    print("Input Score count")
    inputScoreCount = float(input())
    
    return inputScoreCount

def loopAverage(globalScoreCount):
    totalScore = 0
    newScoreCount = globalScoreCount
    for newScoreCount in range(newScoreCount, 1 - 1, -1):
        print("input score")
        inputScore = float(input())
        totalScore = totalScore + inputScore
    
    return totalScore

# Main
# A simple program that tells you the average of your scores
globalScoreCount = inputFunc()
globalTotalScore = loopAverage(globalScoreCount)
globalAverage = averageProcessing(globalScoreCount, globalTotalScore)
averageFunc(globalAverage)
