#a simple program designed to convwert however many miles into other units of mesurement
mile = 1
yards = 1760
feet = yards * 3
inches = feet * 12
kilometer = mile * 1.609344
meter = kilometer * 1000
centimeter = meter * 100
print("input amount of miles")
distance = float(input())
print(str(distance*mile) + "miles long")
print(str(distance*yards)+"yards long")
print(str(distance*feet)+"feet long")
print(str(distance*inches)+"inches long")
print(str(distance*kilometer)+"kilometers long")
print(str(distance*meter)+"meters long")
print(str(distance*centimeter)+"centimeters long")