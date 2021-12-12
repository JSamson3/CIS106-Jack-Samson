# A thing

from os import read
import xml.etree.ElementTree as ET


def read_file():
    file = ET.parse("Final Project\plant_catalog.xml")
    x = file.readlines()
    text = x
    print(text)
    return text


def process_text(text):
    count = 0
    for index in range(len(text)):
        line = text[index].strip()
        if index % 10 == 0:
            common = line.split("<COMMON>")[0].split("</COMMON>")
        elif index % 10 == 1:
            botanitcal = line.split("<BOTANICAL>")[0].split("</BOTANICAL>")[0]
        elif index % 10 == 2:
            zone = line.split("<ZONE>")[0].split("<?ZONE>")[0]
        elif index % 10 == 3:
            light = line.split("<LIGHT>")[0].split("</LIGHT")[0]
        elif index % 10 == 4:
            count = count + 1
            price = line.split("<PRICE>")[0].split("</PRICE>")[0]
            print(f"{common} ({botanitcal}) - {zone} - {light} - {price}"
            f"{price}")
            print(f"{count} percent complete         \r")



def main():
    text = read_file()
    process_text(text)


main()