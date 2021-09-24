def calculateDogYears(age):
    dogYears = age * 7
    
    return dogYears

def displayResults(name, dogYears):
    print(name + " is " + str(dogYears) + " in dog years")

def getAge():
    print("Enter dog's age:")
    age = int(input())
    
    return age

def getName():
    print("Enter dog's name:")
    name = input()
    
    return name

# Main
# A simple program that tells you your dogs age in dog years
name = getName()
age = getAge()
dogYears = calculateDogYears(age)
displayResults(name, dogYears)
