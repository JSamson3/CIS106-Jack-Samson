def display_average(average):
    print("Average Score is " + str(average))

def calculate_average(newScoreCount, totalScore):
    average = newScoreCount / totalScore
    
    return average

def get_average():
    newScoreCount = -1
    totalScore = 0
    inputScore = 0
    while True:    #This simulates a Do Loop
        totalScore = totalScore + inputScore
        newScoreCount = newScoreCount + 1
        print("Input " + str(newScoreCount) + " number of scores" + "Total: " + str(totalScore))
        inputScore = int(input())
        if not(inputScore > -1): break   #Exit loop
    average = calculate_average(totalScore, newScoreCount)
    
    return average

# Main
# A simple program that tells you the average of your scores
average = get_average()
display_average(average)
