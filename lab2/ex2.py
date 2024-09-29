from math import sin, cos

a = float(input("a = "))
b = float(input("b = "))
t = float(input("t = "))

print("x =", round(b*sin(a*(t**2)*cos(2*t))-1))

