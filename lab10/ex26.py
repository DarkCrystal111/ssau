a = input("Введите последовательность: ").split()
b = []
for x in a:
    if x in ["+", "-", "**", "*", "/", "//", "%"]:
        b.append(x)
print(set(b))

