def centimeters(globalDistance):
    centimeters = globalDistance * (1.609344 * (1000 * 100))
    
    return centimeters

def feet(globalDistance):
    feet = globalDistance * (1760 * 3)
    
    return feet

def inches(globalDistance):
    inches = globalDistance * (1760 * (3 * 12))
    
    return inches

def kilometers(globalDistance):
    kilometers = globalDistance * 1.609344
    
    return kilometers

def localDistance():
    print("Input distance in miles")
    globalDistance = float(input())
    
    return globalDistance

def localSystem():
    print("Metric or Imperial?")
    system = input()
    
    return system

def meters(globalDistance):
    meters = globalDistance * (1.609344 * 1000)
    
    return meters

def yards(globalDistance):
    yards = globalDistance * 1760
    
    return yards

# Main
globalDistance = localDistance()
system = localSystem()
if system == "Metric":
    centimeters = centimeters(globalDistance)
    meters = meters(globalDistance)
    kilometers = kilometers(globalDistance)
    print("In metric it would be" + str(kilometers) + " kilometers" + str(meters) + " meters" + str(centimeters) + " centimeters")
else:
    if system == "Imperial":
        yards = yards(globalDistance)
        feet = feet(globalDistance)
        inches = inches(globalDistance)
        print("In Imperial" + str(yards) + " Yards" + str(feet) + " feet" + str(inches) + " inches")
    else:
        print("Invalid")
