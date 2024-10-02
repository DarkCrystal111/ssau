from math import sqrt

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
x = float(input("x: "))

if x < 1.2:
    print("y =", a*pow(x, 2)+b*x+c)
elif x > 1.2:
    print("y =", (a+b*x)/sqrt(pow(x, 2)+1))
else:
    print("y =", a/x+sqrt(pow(x, 2) +1))
