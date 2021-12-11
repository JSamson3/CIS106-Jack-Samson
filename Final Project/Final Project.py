# A thing

from os import read


def read_file():
    file = open("plant_catalog.xml")
    text = file.readlines()
    file.close()
    return text


def main():
    text = read_file()