# A simple program that tells you your weekly monthly and yearly wage
def pay_func():
    print("Hours =" + str(hours))
    print("Rate =" + str(rate))
    print("Weekly " + str(hours * rate))
    print("Monthly " + str(hours * rate * weeksinamonth))
    print("Yearly " + str(hours * rate * weeksinayear))



weeksinaweek = 1
weeksinamonth = 4
weeksinayear = 52

def input_func():
    print("input weekly hours")
    hours = float(input())
    print("input hourly rate")
    rate = float(input())


input_func()
pay_func()