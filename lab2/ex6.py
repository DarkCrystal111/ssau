from math import cos, sqrt

a = float(input("a = "))
b = float(input("b = "))
x = float(input("x = "))

print("y =", round(sqrt(x*b/a)+pow(cos(pow(x+b, 3)), 2)))

