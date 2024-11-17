import string
a = set(input("Введите последовательность: ").split())
b = set(("+", "-", "**", "*", "/", "//", "%", "<", "<=", ">", ">="))
print(a.intersection(b))
