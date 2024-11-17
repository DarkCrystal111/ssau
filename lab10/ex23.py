import string
a = input("Введите последовательность: ").split()
a = set([int(x) if x.isdigit() else x for x in a])
b = set(range(5, 10))
b.update(string.punctuation)
print(a.intersection(b))
