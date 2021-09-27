# A simple program that tells you your weekly monthly and yearly wage
def input_func1():
    print("input weekly hours")
    hours = float(input())
    return hours


def input_func2():
    print("input hourly rate")
    rate = float(input())
    return rate


def processing_func1(hours, rate):
    hourlyrate = hours * rate
    return hourlyrate


def print_func1(hours, rate, hourlyrate):
    print("hours =" + str(hours))
    print("rate =" + str(rate))
    print("Weekly " + str(hourlyrate))


def processing_func2(hours, rate):
    monthlyrate = hours * rate * weeksinamonth
    return monthlyrate


def print_func2(monthlyrate):
    print("Monthly " + str(monthlyrate))


def processing_func3(hours, rate):
    yearlyrate = (hours * rate * weeksinayear)
    return yearlyrate


def print_func3(yearlyrate):
    print("Yearly " + str(yearlyrate))


weeksinaweek = 1
weeksinamonth = 4
weeksinayear = 52


def main():
    hours = input_func1()
    rate = input_func2()
    hourlyrate = processing_func1(hours, rate)
    monthlyrate = processing_func2(hours, rate)
    yearlyrate = processing_func3(hours, rate)
    print_func1(hours, rate, hourlyrate)
    print_func2(monthlyrate)
    print_func3(yearlyrate)


main()
