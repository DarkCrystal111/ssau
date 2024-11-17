a = []
for n in range(1, 13):
    i = float(input(f"Введите {n} элемент списка: "))
    a.append(i)
b = a
n = min(a)
b[a.index(n)] = a[0]
b[0] = n
print(b)
