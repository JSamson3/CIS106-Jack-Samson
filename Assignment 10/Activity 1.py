def averageFunction(average):
    print("Average Score is " + str(average))

def averageProcessing(newScoreCount, totalScore):
    average = totalScore / newScoreCount
    
    return average

def loopAverage():
    newScoreCount = -1
    totalScore = 0
    while True:    #This simulates a Do Loop
        totalScore = totalScore + inputScore
        newScoreCount = newScoreCount + 1
        print("Input " + str(newScoreCount) + " number of scores" + "Total: " + str(totalScore))
        inputScore = float(input())
        if not(inputScore > 0): break   #Exit loop
    average = averageProcessing(totalScore, newScoreCount)
    
    return average

# Main
# A simple program that tells you the average of your scores
average = loopAverage()
averageFunction(average)
