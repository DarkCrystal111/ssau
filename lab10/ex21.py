a = input("Введите последовательность: ").split()
a = [x for x in a if x.isdigit() and 0 <= int(x) < 10]
print(set(a))

