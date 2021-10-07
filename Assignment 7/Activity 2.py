# A simple program that tells you your age in months days and seconds by your choice
yearsinayear = 1
monthsinayear = 12
daysinayear = 365
hoursinayear = 365 * 24
secondsinayear = 365 * (24 * (60 * 60))


def input_func():
    print("input age in years")
    age = float(input())
    return age


def what_age_func():
    print("(M)onths (D)ays (H)ours or (S)econds?")
    response = str(input())
    return response


def output_func(response, age):
    if response == "m" or response == "M":
        print(str(monthsinayear * age) + "Months old")
    elif response == "d" or response == "D":
        print(str(daysinayear * age) + "Days old")
    elif response == "h" or response == "H":
        print(str(age * hoursinayear) + "Hours old")
    elif response == "s" or response == "S":
        print(str(age * secondsinayear) + "Seconds old")
    else:
        print("invalid selection")


def main():
    response = what_age_func()
    age = input_func()
    output_func(response, age)


main()