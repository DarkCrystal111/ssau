from math import sin

a = float(input("a = "))
b = float(input("b = "))
x = float(input("x = "))

print("y =", round(x**2*(x+1)/(b-pow(sin(x+a), 2))))

