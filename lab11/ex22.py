a = []
for n in range(1, 21):
    i = int(input(f"Введите {n} элемент списка: "))
    if i >= 0:
        a.append(i)
print("Всего", len(a), "положительных чисел в списке")
