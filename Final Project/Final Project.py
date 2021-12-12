# A thing

from os import read


def read_file():
    file = open("Final Project\plant_catalog.xml")
    text = file.readlines()
    file.close()
    print(text)
    return text


def process_text(text):
    for index in range(len(text)):
        line = text[index].strip()
        if index % 4 == 0:
            common = line.split("<COMMON>")[0].split("</COMMON>")
        elif index % 4 == 1:
            botanitcal = line.split("<BOTANICAL>")[0].split("</BOTANICAL>")[0]
        elif index % 4 == 2:
            zone = line.split("<ZONE>")[0].split("<?ZONE")[0]
        elif index % 4 == 3:
            light = line.split("<LIGHT>")[0].split("</LIGHT")[0]
        elif index % 4 == 4:
            price = line.split("<PRICE>")[0].split("</PRICE>")[0]
            print(f"{common} ({botanitcal}) - {zone} - {light} - {price}")


def main():
    text = read_file()
    process_text(text)


main()