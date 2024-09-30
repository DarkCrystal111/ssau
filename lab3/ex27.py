a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

print("Всего двухзначных чисел: ", sum(len(str(abs(x))) == 2 for x in (a,b,c)))
