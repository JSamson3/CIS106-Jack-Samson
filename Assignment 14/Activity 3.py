# A program that pulls out tags from html and txt files

def open_file():
    print("input")
    text = open(str(input()), "r")
    print(text)
    file = text.read().replace("<", ">").strip().split(">").join()
    text.close()
    print(file)
    return file


def parse_file1(file):
    tags = []
    if file.count("h1") >= 0:
        file.remove("h1")
        file.remove("/h1")
        tags.append("<h1>")
        tags.append("</h1>")
    print(tags)
    return tags


def main():
    file = open_file()
    tags = parse_file1(file)


main()