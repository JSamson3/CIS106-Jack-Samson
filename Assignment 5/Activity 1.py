# A simple program that tells you your weekly monthly and yearly wage
def input_func1():
    print("input weekly hours")
    global hours
    hours = float(input())

def input_func2():
    print("input hourly rate")
    global rate
    rate = float(input())
    

def pay_func():
    input_func1()
    input_func2()
    print("Hours =" + str(hours))
    print("Rate =" + str(rate))
    print("Weekly " + str(hours * rate))
    print("Monthly " + str(hours * rate * weeksinamonth))
    print("Yearly " + str(hours * rate * weeksinayear))



weeksinaweek = 1
weeksinamonth = 4
weeksinayear = 52


pay_func()