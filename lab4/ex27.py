a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
i = float(input("i: "))

if i < 4:
    print("y =", (a/i)+b*pow(i, 2)+c)
elif 4 <= i < 6:
    print("y =", i)
else:
    print("y =", a*i+b*pow(i, 3))