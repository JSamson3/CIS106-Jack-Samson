#A simple program that tells you your dogs age in dog years
def age_func():
    print(str(name) + " is " + str(dogyears) + " years old in dog years")
print("input dog name")
name = str(input())
print("input dog age")
age = float(input())
dogyears = (age*7)
age_func()
