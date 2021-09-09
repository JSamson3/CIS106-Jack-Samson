# A simple program that tells you your weekly monthly and yearly wage
hours = float(input())
rate = float(input())
print("Weekly " + str(hours * rate))
print("Monthly " + str(hours * rate * 4))
print("Yearly " + str(hours * rate * 52))
