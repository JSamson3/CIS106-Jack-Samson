# A simple program that prints out addresses for who knows what purpose

def read_file():
    file = open("addresses.txt")
    text = file.readlines()
    file.close()
    return text


def process_text(text):
    for index in range(len(text)):
        line = text[index].strip()
        if index % 4 == 0:
            firstname = line.split()[0]
            lastname = line.split()[1]
        elif index % 4 == 1:
            address = line
        elif index % 4 == 2:
            city = line.split(",")[0]
            state = line.split(",")[1].split()[0]
            zip = line.split(",")[1].split()[1]
            print(f"{lastname}, {firstname}, {address},"
                f" {city}, {state}, {zip}")


def main():
    text = read_file()
    process_text(text)


main()
