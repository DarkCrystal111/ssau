from math import cos, sqrt

a = float(input("a = "))
b = float(input("b = "))
x = float(input("x = "))

print("y =", round(pow(cos(x**3), 2)-(x/sqrt(a**2+b**2))))

