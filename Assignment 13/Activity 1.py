#A simple program that asks for your name
def get_first_name():
    print("input first name")
    first = input(str())
    return first


def get_last_name():
    print("input last name")
    last = input(str())
    return last


def display_answer(first, last):
    print(last, first[0:1] + ".")


def main():
    first = get_first_name()
    last = get_last_name()
    display_answer(first, last)

main()
