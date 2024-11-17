a = input("Введите последовательность: ").split()
a = set([int(x) if x.isdigit() else x for x in a])
b = set(("+", "-", "**", "*", "/", "//", "%"))
print(a.intersection(b))
