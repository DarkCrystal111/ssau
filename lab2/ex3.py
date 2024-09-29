from math import sin, sqrt

a = float(input("a = "))
b = float(input("b = "))
x = float(input("x = "))

print("y =", round(sqrt(x**2+b)-b**2*pow(sin(x+a), 3)/x))
