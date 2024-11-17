a = []
for n in range(1, 17):
    i = int(input(f"Введите {n} элемент списка: "))
    if n % 2 == 0:
        a.append(i)
print("Новая последовательность:", *a)
