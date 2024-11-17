a = []
for n in range(1, 21):
    i = int(input(f"Введите {n} элемент списка: "))
    a.append(i)
b = a
n = min(a)
b[a.index(n)] = a[-1]
b[-1] = n
print(b)
