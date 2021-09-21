# A simple program that tells you your weekly monthly and yearly wage
def pay_func():
    print("hours =" + str(hours))
    print("rate =" + str(rate))
    print("weekly " + str(hours * rate))
    print("monthly " + str(hours * rate * weeksinamonth))
    print("yearly " + str(hours * rate * weeksinayear))
weeksinaweek = 1
weeksinamonth = 4
weeksinayear = 52
print("input weekly hours")
hours = float(input())
print("input hourly rate")
rate = float(input())
pay_func()
