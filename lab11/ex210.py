a = []
for n in range(1, 26):
    i = int(input(f"Введите оценку {n} студента: "))
    if i == 2:
        a.append(i)
print(len(a), "студентов не допущены к экзамену")
