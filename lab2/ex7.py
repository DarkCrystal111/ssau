from math import sin, sqrt

a = float(input("a = "))
b = float(input("b = "))
x = float(input("x = "))

print("y =", round(pow(sin(pow(x**2+a, 2)), 3)-sqrt(x/b)))

