# A simple program that tells you your age in months days and seconds by your choice
yearsinayear = 1
monthsinayear = 12
daysinayear = 365
hoursinayear = 365 * 24
secondsinayear = 31536000


def input_func():
    print("input age in years")
    age = float(input())
    return age


def what_age_func():
    print("(M)onths (D)ays (H)ours or (S)econds?")
    response = str(input())
    return response


def months_processing(age):
    monthsold = age * monthsinayear
    return monthsold


def days_processing(age):
    daysold = age * daysinayear
    return daysold


def hour_processing(age):
    hoursold = age * hoursinayear
    return hoursold


def seconds_processing(age):
    secondsold = age * secondsinayear
    return secondsold


def output_func(response, age, monthsold, daysold, hoursold, secondsold):
    if response == "m" or response == "M":
        print(str(monthsold) + "Months old")
    elif response == "d" or response == "D":
        print(str(daysold) + "Days old")
    elif response == "h" or response == "H":
        print(str(hoursold) + "Hours old")
    elif response == "s" or response == "S":
        print(str(secondsold) + "Seconds old")
    else:
        print("invalid selection")


def main():
    age = input_func()
    response = what_age_func()
    monthsold = months_processing(age)
    daysold = days_processing(age)
    hoursold = hour_processing(age)
    secondsold = seconds_processing(age)
    output_func(response, age, monthsold, daysold, hoursold, secondsold)


main()