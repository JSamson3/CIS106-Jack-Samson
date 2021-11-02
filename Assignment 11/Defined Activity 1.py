# A program that tells you how many days are in a month
Months = ["jan", "feb", "mar"]
Days = [31, 28, 31]
month_input = input(("enter month number"))
year = int(input("Enter Year: "))
if year % 4 == 0 and year % 100 != 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
    print(year, "is not a Leap Year")
elif year % 400 ==0:
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")
