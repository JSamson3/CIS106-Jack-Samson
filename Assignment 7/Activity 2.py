# A program that tells you your age in months days and seconds by your choice

MONTHS_IN_A_YEAR = 12
DAYS_IN_A_YEAR = 365
HOURS_IN_A_YEAR = 365 * 24
SECONDS_IN_A_YEAR = 365 * 24 * 60 * 60


def get_age():
    print("input age in years")
    age = float(input())
    return age


def get_choice():
    print("(M)onths (D)ays (H)ours or (S)econds?")
    response = str(input())
    return response


def process_months(age):
    months = age * MONTHS_IN_A_YEAR
    return months


def process_days(age):
    days = age * DAYS_IN_A_YEAR
    return days


def process_hours(age):
    hours = age * HOURS_IN_A_YEAR
    return hours


def process_seconds(age):
    seconds = age * SECONDS_IN_A_YEAR
    return seconds


def display_output(response, age, months, days, hours, seconds):
    if response == "m" or response == "M":
        print(str(months) + "Months old")
    elif response == "d" or response == "D":
        print(str(days) + "Days old")
    elif response == "h" or response == "H":
        print(str(hours) + "Hours old")
    elif response == "s" or response == "S":
        print(str(seconds) + "Seconds old")
    else:
        print("invalid selection")


def main():
    age = get_age()
    response = get_choice()
    months = process_months(age)
    days = process_days(age)
    hours = process_hours(age)
    seconds = process_seconds(age)
    display_output(response, age, months, days, hours, seconds)


main()
