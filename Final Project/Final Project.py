# A program that reads an xml file and prints out the data contained inside


import os
import os.path
import sys


def read_file():
    if os.path.isfile("plant_catalog.xml") is True:
        try:
            if os.stat("plant_catalog.xml").st_size > 0:
                file = open("plant_catalog.xml")
                text = file.readlines()
            else:
                print("No file")
                sys.exit()
        except OSError:
            print("An error has occured")
            sys.exit()
        return text
    else:
        print("File does not exist")
        sys.exit()


def process_text(text):
    count = 0
    total = 0
    for index in range(len(text)):
        line = text[index].strip()
        if line.index("<") is False:
            print("No data")
            sys.exit()
        if index % 8 == 3:
            common = line.split(">")[1].split("</")[0]
        elif index % 8 == 4:
            botanitcal = line.split(">")[1].split("</")[0]
        elif index % 8 == 5:
            zone = line.split(">")[1].split("</")[0]
        elif index % 8 == 6:
            light = line.split(">")[1].split("</")[0]
        elif index % 8 == 7:
            count = count + 1
            try:
                price = float(line.split(">$")[1].split("</")[0])
            except:
                print("missing data")
            total = total + price
            print(f"{common} ({botanitcal}) - {zone} - {light} - ${price}")
            print(f"{count} items - ${round(total / count, 2)} average price")


def main():
    text = read_file()
    process_text(text)


main()