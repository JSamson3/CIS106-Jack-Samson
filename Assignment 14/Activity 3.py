# A program that pulls out tags from html and txt files

def open_file():
    print("input")
    text = open(str(input()))
    file = text.read()
    print(file)
    return file


def parse_file1(file):
    tags = []
    if file.find("<h1>") >= 0:
        file.split("<h1>")
        file.split("</h1>")
        tags.append("<h1>")
        tags.append("</h1>")
    print(tags)
    return tags



def main():
    file = open_file()
    tags = parse_file1(file)


main()