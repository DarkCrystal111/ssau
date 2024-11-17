a = []
for n in range(1, 16):
    i = float(input(f"Введите {n} элемент списка: "))
    a.append(i)
b = a
n = max(a)
b[a.index(n)] = a[-1]
b[-1] = n
print(b)
