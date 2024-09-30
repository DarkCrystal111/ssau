a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

print("Всего отрицательных чисел: ", sum(x < 0 for x in (a,b,c)))
