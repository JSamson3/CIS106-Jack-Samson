# A simple program that tells you your age in months days and seconds
monthsinayear = 12
daysinayear = 365
hoursinayear = 365 * 24
secondsinayear = 365 * (24 * (60 * 60))
age = float(input())
print(str(age * monthsinayear) + " months old")
print(str(age * daysinayear) + " days old")
print(str(age * hoursinayear) + " hours old")
print(str(age * secondsinayear) + " Seconds old")
