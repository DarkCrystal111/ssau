import string
a = input("Введите последовательность: ").split()
a = set([int(x) if x.isdigit() else x for x in a])
b = set(string.punctuation)
b.update(("//", "**"))
print(a.intersection(b))
