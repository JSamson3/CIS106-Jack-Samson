#A simple program that tells you your weekly monthly and yearly wage
def pay_func():
    print("hours =" + str(hours))
    print("rate =" + str(rate))
    print("weekly " + str(hours * rate))
    print("monthly " + str(hours * rate * weeks_in_a_month))
    print("yearly " + str(hours * rate * weeks_in_a_year))
    
weeks_in_a_week = 1
weeks_in_a_month = 4
weeks_in_a_year = 52

print("input weekly hours")
hours = float(input())
print("input hourly rate")
rate = float(input())

pay_func()
