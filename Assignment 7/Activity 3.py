def centimeters(globalDistance):
    centimeters = globalDistance * (1.609344 * (1000 * 100))
    
    return centimeters

def feet(globalDistance):
    feet = globalDistance * (1760 * 3)
    
    return feet

def imperialEnd(inches, feet, yards, globalDistance):
    print("In Imperial " + str(yards) + " Yards " + str(feet) + " feet " + str(inches) + " inches ")

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
    print("Metric or US?")
    system = input()
    
    return system

def meters(globalDistance):
    meters = globalDistance * (1.609344 * 1000)
    
    return meters

def metricEnd(kilometers, meters, centimeters, globalDistance):
    print("In metric it would be " + str(kilometers) + " kilometers " + str(meters) + " meters " + str(centimeters) + " centimeters ")

def yards(globalDistance):
    yards = globalDistance * 1760
    
    return yards

# Main
# A simple program that converts units to what system you choose
globalDistance = localDistance()
system = localSystem()
if system == "Metric":
    centimeters = centimeters(globalDistance)
    meters = meters(globalDistance)
    kilometers = kilometers(globalDistance)
    metricEnd(meters, kilometers, centimeters, globalDistance)
else:
    if system == "US":
        yards = yards(globalDistance)
        feet = feet(globalDistance)
        inches = inches(globalDistance)
        imperialEnd(inches, feet, yards, globalDistance)
    else:
        print("Invalid")
