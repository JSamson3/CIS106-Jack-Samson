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
        print(year_input, "is a Leap Year")
        days_in_year[1] = 29
    elif year_input % 100 == 0:
        print(year_input, "is not a Leap Year")
    elif year_input % 400 ==0:
        print(year_input, "is a Leap Year")
        days_in_year[1] = 29
    else:
        print(year_input, "is not a Leap Year")
    return days_in_year


def display_array(month_input, days_in_year):
    months_in_year = ["jan", "feb", "mar", "apr", "may",
     "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    print(months_in_year[month_input])
    print(days_in_year[month_input])


def loop_function(month_input, year_input):
    while 11 > month_input > 0 or year_input > 0:
        month_input = get_month()
        year_input = get_year()
        days_in_year = process_leap(year_input)
        display_array(month_input, days_in_year)


def main():
    year_input = get_year()
    month_input = get_month()
    days_in_year = process_leap(year_input)
    display_array(month_input, days_in_year)
    loop_function(month_input, year_input)


main()