# A program that tells you how many days are in a month


def get_month():
    print("enter month number")
    month_input = int(input()) - 1
    return month_input


def get_year():
    print("enter year")
    year_input = int(input())
    return year_input


def process_leap(year_input): 
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 30]   
    if year_input % 4 == 0 and year_input % 100 != 0:
        days[1] = 29
    elif year_input % 400 == 0:
        days[1] = 29
    else:
        days[1] = 28
    return days


def display_array(month_input, days, year_input):
    months = ["January", "Febuary", "March", "April", "May",
     "June", "July", "August", "September",
      "October", "November", "December"]
    print(months[month_input], year_input, "has", days[month_input], "days")


def loop_function(month_input, year_input, days):
    display_array(month_input, days, year_input)
    while 11 > month_input > 0 or year_input > 0:
        year_input = get_year()
        if year_input <= -1:
            print("invalid year")
            break
        month_input = get_month()
        if month_input >= 11 or month_input <= 0:
            print("invalid month")
            break
        days = process_leap(year_input)
        display_array(month_input, days, year_input)


def main():
    year_input = get_year()
    month_input = get_month()
    days = process_leap(year_input)
    loop_function(month_input, year_input, days)


main()