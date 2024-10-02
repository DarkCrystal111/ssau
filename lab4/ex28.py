from math import sqrt, sin, cos

a = float(input("a: "))
b = float(input("b: "))
t = float(input("t: "))

if t < 0.1:
    print("y =", sqrt(a*pow(t, 2)+b*sin(t)+1))
elif t == 0.1:
    print("y =", a*t+b)
else:
    print("y =", sqrt(a*pow(t, 2)+b*cos(t)+1))