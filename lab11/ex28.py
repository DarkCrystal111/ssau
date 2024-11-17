a = int(input("Сколько дней в марте?: "))
days = []
for n in range(1, a+1):
    i = int(input(f"Введите температуру за {n} марта: "))
    if i < 0:
        days.append(i)
print("Температура опускалась ниже нуля", len(days), "дней")
