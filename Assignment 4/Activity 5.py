# a simple program to calculate square yards
print("input X feet")
x_feet = float(input())

print("input Y feet")
y_feet = float(input())

squarefootage = x_feet * y_feet
squareyards = squarefootage / 9

print(str(x_feet) + "length")
print(str(y_feet) + "width")

print(str(squarefootage) + "square footage")
print(str(squareyards) + "square yards")
