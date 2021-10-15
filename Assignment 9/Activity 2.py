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
    while newScoreCount > 0:
        print("Input " + str(newScoreCount) + " number of scores" + "Total: " + str(totalScore))
        inputScore = float(input())
        newScoreCount = newScoreCount - 1
        totalScore = totalScore + inputScore
    
    return totalScore

# Main
# A simple program that tells you the average of your scores
globalScoreCount = inputFunc()
globalTotalScore = loopAverage(globalScoreCount)
globalAverage = averageProcessing(globalScoreCount, globalTotalScore)
averageFunc(globalAverage)
