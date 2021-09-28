#a simple program designed to convert miles into other units of mesurement
mile = 1
yards = 1760
feet = yards * 3
inches = feet * 12
kilometer = mile * 1.609344
meter = kilometer * 1000
centimeter = meter * 100


def input_func():
    print("input amount of miles")
    distance = float(input())
    return distance


def processing_func1(distance):
    yardslong = distance * yards
    return yardslong


def processing_func2(distance):
    feetlong = distance * feet
    return feetlong


def processing_func3(distance):
    incheslong = distance * inches
    return incheslong


def processing_func4(distance):
    kilometerlong = distance * kilometer
    return kilometerlong


def processing_func5(distance):
    meterslong = distance * meter
    return meterslong


def processing_func6(distance):
    centimeterslong = distance * meter
    return centimeterslong


def print_func(distance, yardslong, feetlong, incheslong, kilometerlong, meterslong, centimeterslong):
    print(str(distance) + "miles long")
    print(str(yardslong)+"yards long")
    print(str(feetlong)+"feet long")
    print(str(incheslong)+"inches long")
    print(str(kilometerlong)+"kilometers long")
    print(str(meterslong)+"meters long")
    print(str(centimeterslong)+"centimeters long")


def main():
    distance = input_func()
    yardslong = processing_func1(distance)
    feetlong = processing_func2(distance)
    incheslong = processing_func3(distance)
    kilometerlong = processing_func4(distance)
    meterslong = processing_func5(distance)
    centimeterslong = processing_func6(distance)
    print_func(distance, yardslong, feetlong, incheslong, kilometerlong, meterslong, centimeterslong)


main()