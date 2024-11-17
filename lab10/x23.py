a = input("Введите последовательность: ").split()
b = []
for x in a:
    if x.isdigit() and 5 <= int(x) < 10 or x in ["+", "-", "**", "*", "/", "//", "%"]:
        b.append(x)
print(set(b))

