a = input("Введите последовательность: ").split()
a = [int(x) for x in a if x.isdigit()]
b = set(range(0, 10))
print(set(a).intersection(b))

