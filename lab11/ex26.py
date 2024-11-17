a = []
for n in range(1, 21):
    i = int(input(f"Введите {n} элемент списка: "))
    a.append(i)
print("Наименьший элемент:", min([x for x in a if x > 0]))
