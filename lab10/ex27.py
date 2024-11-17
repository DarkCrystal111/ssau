import string
a = set(input("Введите последовательность: ").upper())
b = set(string.punctuation)
b.update(("E", "F", "G", "H", "I", "J", "K", "L", "M", "N"))
print(a.intersection(b))
