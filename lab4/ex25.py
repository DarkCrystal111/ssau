from math import e, cos, sin, sqrt

a = float(input("a: "))
x = float(input("x: "))

if x > a:
    print("y =", x*pow(sqrt(x-a), 1/3))
elif x < a:
    t = float(input("t: "))
    print("y =", pow(e, (-a*t))*cos(a*x))
else:
    print("y =", x*sin(a*x))