a = []
for n in range(1, 21):
    i = int(input(f"Введите {n} элемент списка: "))
    a.append(i)
b = a
n = max(a)
b[a.index(n)] = a[0]
b[0] = n
print(b)
