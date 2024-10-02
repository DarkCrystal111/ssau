from math import sqrt, log, pi

a = float(input("a: "))
x = float(input("x: "))

if x < 1.4:
    print("y =", pi*pow(x,2)-7/pow(x, 2))
elif x > 1.4:
    print("y =", log(x)+7*sqrt(abs(x+a)))
else:
    print("y =", a*pow(x,3)+7*sqrt(x))