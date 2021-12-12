# A program that reads an xml file and prints out the data contained inside


import os
import os.path
import sys


def user_input():
    print("input")
    answer = str(input())
    return answer


def read_file():
    if os.path.exists("plant_catalog.xml") == True:
        try:
            if os.stat("plant_catalog.xml").st_size > 0:
                file = open("plant_catalog.xml")
                text = file.readlines()
            else:
                print("Empty file")
                sys.exit()
        except OSError:
            print("An error has occured")
            sys.exit()
        return text
    else:
        print("File does not exist")
        sys.exit()


def process_text(text, answer):
    count = 0
    total = 0
    if answer == "" or int(answer) > len(text):
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
                    print(f"{common} ({botanitcal}) - {zone} - {light}")
                    print(f"{count} counted average:{round(price / count, 2)}$\r")
    else:
        try:
            answer = int(answer)
            for index in range(answer*8):
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
                    print(f"{count} counted average:{round(price / count, 2)}$\r")    
        except OSError:
            print("Bad Data")
            sys.exit


def main():
    answer = user_input()
    text = read_file()
    process_text(text, answer)


main()