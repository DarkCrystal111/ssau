n = int(input("Введите количество оценок: "))
a = []
for _ in range(1, n+1):
    a.append(int(input(f"Введите оценку {_}: ")))
print("Все оценки:", *a, "Средний балл:", sum(a)/n)
