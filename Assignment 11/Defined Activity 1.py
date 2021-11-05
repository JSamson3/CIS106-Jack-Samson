# A program that tells you how many days are in a month


def get_month():
    print("enter month number")
    month_input = int(input()) - 1
    if 11 < month_input or month_input < -1:
        print("invalid")
        quit()
    return month_input


def get_year():
    print("enter year")
    year_input = int(input())
    if year_input < 0:
        print("invalid")
        quit()
    return year_input


def process_leap(year_input): 
    days_in_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 30]   
    if year_input % 4 == 0 and year_input % 100 != 0:
        days_in_year[1] = 29
    elif year_input % 400 ==0:
        days_in_year[1] = 29
    else:
        days_in_year[1] = 28
    return days_in_year


def display_array(month_input, days_in_year, year_input):
    months_in_year = ["january", "febuary", "march", "april", "may",
     "june", "july", "august", "september", "october", "november", "december"]
    print(months_in_year[month_input], year_input, "has", days_in_year[month_input], "days")


def loop_function(month_input, year_input):
    while 11 > month_input > 0 or year_input > 0:
        month_input = get_month()
        year_input = get_year()
        days_in_year = process_leap(year_input)
        display_array(month_input, days_in_year, year_input)
        if month_input >= 11 or month_input <= 0:
            break
        if year_input >= 0:
            break


def main():
    year_input = get_year()
    month_input = get_month()
    days_in_year = process_leap(year_input)
    display_array(month_input, days_in_year, year_input)
    loop_function(month_input, year_input)


main()