a = []
for n in range(1, 19):
    i = int(input(f"Введите {n} элемент списка: "))
    if i % 2 == 0:
        a.append(i)
if len(a) > 0:
    print(a)
else:
    print("Нет четных элементов")
