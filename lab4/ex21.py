from math import log, e, cos
a = float(input("a: "))
b = int(input("b: "))
t = float(input("t: "))

if 1 <= t <= 2:
    print("y =", a*pow(t, 2)*log(t))
elif t < 1:
    print("y =", 1)
else:
    print("y =", pow(e, a*t)*cos(b*t))