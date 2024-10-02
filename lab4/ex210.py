from math import sqrt, log, cos, sin

t = float(input("t: "))
x = float(input("x: "))

if x < 0.5:
    print("y =", (log(x)+pow(x, 2))/sqrt(x+t))
elif x == 0.5:
    print("y =", sqrt(x+t)+1/x)
else:
    print("y =", cos(x)+pow(sin(x), 2))