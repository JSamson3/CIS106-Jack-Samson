# A simple program that tells you your weekly monthly and yearly wage
def input_func1():
    print("input weekly hours")
    global hours
    hours = float(input())
    return hours


def input_func2():
    print("input hourly rate")
    global rate
    rate = float(input())
    return rate


def pay_func1():
    print("hours =" + str(hours))
    print("rate =" + str(rate))
    print("Weekly " + str(hours * rate))


def pay_func2():
    print("Monthly " + str(hours * rate * weeksinamonth))


def pay_func3():
    print("Yearly " + str(hours * rate * weeksinayear))


weeksinaweek = 1
weeksinamonth = 4
weeksinayear = 52


def main():
    input_func1()
    input_func2()
    pay_func1()
    pay_func2()
    pay_func3()


main()