a = []
for n in range(1, 15):
    i = float(input(f"Введите {n} элемент списка: "))
    a.append(i)
print(*[x for x in a if 0 < x < 1])