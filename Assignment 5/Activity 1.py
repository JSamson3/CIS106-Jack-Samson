# A simple program that tells you your weekly monthly and yearly wage

WEEKS_IN_A_MONTH = 4
WEEKS_IN_A_YEAR = 52


def input_hours():
    print("input weekly hours")
    hours = float(input())
    return hours


def input_rate():
    print("input hourly rate")
    rate = float(input())
    return rate


def process_weekly(hours, rate):
    hourlyrate = hours * rate
    return hourlyrate


def print_weekly(hours, rate, hourlyrate):
    print("hours =" + str(hours))
    print("rate =" + str(rate))
    print("Weekly " + str(hourlyrate))


def process_monthly(hours, rate):
    monthly_rate = hours * rate * WEEKS_IN_A_MONTH
    return monthly_rate


def print_monthly(monthly_rate):
    print("Monthly " + str(monthly_rate))


def process_yearly(hours, rate):
    yearly_rate = (hours * rate * WEEKS_IN_A_YEAR)
    return yearly_rate


def print_yearly(yearly_rate):
    print("Yearly " + str(yearly_rate))


def main():
    hours = input_hours()
    rate = input_rate()

    hourly_rate = process_weekly(hours, rate)
    monthly_rate = process_monthly(hours, rate)
    yearly_rate = process_yearly(hours, rate)
    
    print_weekly(hours, rate, hourly_rate)
    print_monthly(monthly_rate)
    print_yearly(yearly_rate)


main()
