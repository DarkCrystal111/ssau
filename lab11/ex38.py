a = []
for n in range(1, 13):
    i = int(input(f"Введите {n} элемент списка: "))
    a.append(i)
a = [x for x in a if x < 0] + [x for x in a if x >= 0]
print(a)

