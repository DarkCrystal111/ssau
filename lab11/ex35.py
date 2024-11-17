a = []
for n in range(1, 11):
    i = float(input(f"Введите {n} элемент списка: "))
    a.append(i)
print(sorted(a, reverse=True))
