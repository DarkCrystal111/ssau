from math import log

b = float(input("b: "))
x = float(input("x: "))

if b*x < 1:
    print("y =", b*x-log(b*x))
elif b*x == 1:
    print("y =", 1)
else:
    print("y =", b*x+log(b*x))