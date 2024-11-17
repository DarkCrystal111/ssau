import string
a = set(input("Введите последовательность: ").upper())
b = set(string.punctuation)
print(a.intersection(b))
