import string
a = input("Введите последовательность: ").split()
a = set([int(x) if x.isdigit() else x for x in a])
b = set(range(0, 6))
b.update(string.ascii_letters)
print(a.intersection(b))
