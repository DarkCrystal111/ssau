a = []
for n in range(1, 16):
    i = int(input(f"Введите {n} элемент списка: "))
    a.append(i)
print("Наименьший элемент:", min(a), "и его индекс:", a.index(min(a)))
