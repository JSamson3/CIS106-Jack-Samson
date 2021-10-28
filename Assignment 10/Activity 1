def averageFunction(average):
    print("Average Score is " + str(average))

def averageProcessing(newScoreCount, totalScore):
    average = totalScore / newScoreCount
    
    return average

def loopAverage():
    newScoreCount = -1
    totalScore = 0
    while True:    #This simulates a Do Loop
        newScoreCount = newScoreCount + 1
        print("Input " + str(newScoreCount) + " number of scores" + "Total: " + str(totalScore))
        inputScore = float(input())
        totalScore = totalScore + inputScore
        if not(inputScore > 0): break   #Exit loop
    average = averageProcessing(totalScore, newScoreCount)
    
    return average

# Main
average = loopAverage()
averageFunction(average)

# A simple program that tells you the average of your scores
