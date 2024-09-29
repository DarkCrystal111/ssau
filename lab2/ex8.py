from math import cos

a = float(input("a = "))
b = float(input("b = "))
x = float(input("x = "))

print("y =", round((a**(2*x)+(b**(-x))*(cos(a+b)*x))/(x+1)))
