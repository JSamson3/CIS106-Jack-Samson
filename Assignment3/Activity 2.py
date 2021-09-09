# A simple program that tells you your age in months days and seconds
age = float(input())
print(str(age * 12) + " months old")
print(str(age * 365) + " days old")
print(str(age * (365 * 24)) + " hours old")
print(str(age * (365 * (24 * (60 * 60)))) + " Seconds old")
