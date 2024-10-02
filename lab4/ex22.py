from math import pi, sqrt, log

a = float(input("a: "))
x = float(input("x: "))
if x < 1.3:
    print("x =", pi*pow(x, 2)-7/pow(x, 2))
elif x > 1.3:
    print("x =", log(x+7*sqrt(x)))
else:
    print("x =", a*pow(x, 3)+7*sqrt(x))