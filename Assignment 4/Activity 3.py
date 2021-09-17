# A simple program designed to convert miles into other units of mesurement.

MILES_PER_MILE = 1
YARDS_PER_MILE = 1760
FEET_PER_MILE = YARDS_PER_MILE * 3
INCHES_PER_MILE = FEET_PER_MILE * 12

print("input amount of miles")
distance = float(input())

miles = distance * MILES_PER_MILE
yards = distance * YARDS_PER_MILE
feet = distance * FEET_PER_MILE
inches = distance * INCHES_PER_MILE

print(str(miles) + "miles long")
print(str(yards) + "yards long")
print(str(feet) + "feet long")
print(str(inches) + "inches long")
