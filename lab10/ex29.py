import string
a = input("Введите последовательность: ").split()
a = set([int(x) if x.isdigit() else x for x in a])
b = set(string.punctuation)
b.update(("//", 0,1,2,3,4,5,6,7,8,9))
print(a.intersection(b))
