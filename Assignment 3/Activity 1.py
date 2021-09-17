# A simple program that tells you your weekly monthly and yearly wage
weeksinaweek = 1
weeksinamonth = 4
weeksinayear = 52
hours = float(input())
rate = float(input())
print("Hours =" + str(hours))
print("Rate =" + str(rate))
print("Weekly " + str(hours * rate))
print("Monthly " + str(hours * rate * weeksinamonth))
print("Yearly " + str(hours * rate * weeksinayear))
