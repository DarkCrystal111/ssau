from math import e, cos, sin

a = float(input("a: "))
b = float(input("b: "))
x = float(input("x: "))

if x < 2.8:
    print("y =", (a+b)/(pow(e, x)+cos(x)))
elif 2.8 <= x < 6:
    print("y =", (a+b)/(x+1))
else:
    print("y =", pow(e, x)+sin(x))