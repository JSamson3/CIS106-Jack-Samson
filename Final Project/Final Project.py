# A program that reads an xml file and prints out the data contained inside


from os import read
import sys


def read_file():
    try:
        file = open("plant_catalog.xml")
        text = file.readlines()
    except:
        print("an error has occured")
        sys.exit()
    return text


def process_text(text):
    count = 0
    total = 0
    for index in range(len(text)):
        line = text[index].strip()
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
            price = float(line.split(">$")[1].split("</")[0])
            total = total + price
            print(f"{common} ({botanitcal}) - {zone} - {light} - {price}")
            print(f"{count} counted {round(count / price, 2)}\r")


def main():
    text = read_file()
    process_text(text)


main()