import string
a = input("Введите последовательность: ").split()
a = set([int(x) if x.isdigit() else x.upper() for x in a])
b = set(("A", "B", "C", "D", "E", "F", "X", "Y", "Z"))
print(a.intersection(b))
