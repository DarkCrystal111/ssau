a = input("Введите последовательность: ").split()
b = []
for x in a:
    if x in ["+", "-", "**", "*", "/", "//", "%"] or x.isdigit():
        b.append(x)
print(set(b))

