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
    print("hours =" + str(hours))
    print("rate =" + str(rate))
    print("Weekly " + str(hours * rate))
    print("Monthly " + str(hours * rate * weeks_in_a_month))
    print("Yearly " + str(hours * rate * weeks_in_a_year))


weeks_in_a_week = 1
weeks_in_a_month = 4
weeks_in_a_year = 52


pay_func()
