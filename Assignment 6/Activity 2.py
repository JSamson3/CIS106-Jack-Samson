# A simple program that tells you your age in months days and seconds
yearsinayear = 1
monthsinayear = 12
daysinayear = 365
hoursinayear = 365 * 24
secondsinayear = 365 * (24 * (60 * 60))


def input_func():
    print("input age in years")
    age = float(input())
    return age

def processing_func1(age):
    yearsold = age * yearsinayear
    return yearsold


def processing_func2(age):
    monthsold = age * monthsinayear
    return monthsold


def processing_func3(age):
    daysold = age * daysinayear
    return daysold


def processing_func4(age):
    hoursold = age * hoursinayear
    return hoursold


def processing_func5(age):
    secondsold = age * secondsinayear
    return secondsold


def print_func(yearsold, monthsold, daysold, hoursold, secondsold):
    print(str(yearsold) + " Years old")
    print(str(monthsold) + " months old")
    print(str(daysold) + " days old")
    print(str(hoursold) + " hours old")
    print(str(secondsold) + " Seconds old")


def main():
    age = input_func()
    yearsold = processing_func1(age)
    monthsold = processing_func2(age)
    daysold = processing_func3(age)
    hoursold = processing_func4(age)
    secondsold = processing_func5(age)
    print_func(yearsold, monthsold, daysold, hoursold, secondsold)


main()
