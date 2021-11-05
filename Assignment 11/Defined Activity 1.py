# A program that tells you how many days are in a month


def get_month():
    print("enter month number")
    month = int(input())
    return month


def get_year():
    print("enter year")
    year = int(input())
    return year


def get_month_name(month):
    months = ["January", "February", "March", "April", "May",
     "June", "July", "August", "September",
      "October", "November", "December"]

    if month < 1 or month > 12:
        return "Unknown"
    
    return months[month - 1]


def get_month_days(year, month):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]   

    if process_leap(year):
        days[1] = 29

    if month < 1 or month > 12:
        return "Unknown"
    
    return days[month - 1]


def process_leap(year): 
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


def display_results(month_name, month_days, year):
    print(month_name, year, "has", month_days, "days")


def main():
    while True:
        year = get_year()
        if year <= 0:
            break

        month = get_month()
        if month < 1 or month > 12:
            break

        month_name = get_month_name(month)
        month_days = get_month_days(year, month)

        display_results(month_name, month_days, year)


main()
