a = input("Введите последовательность: ").split()
b = []
for x in a:
    if x.isalpha() and x.upper() in ["A", "B", "C", "D", "E", "F", "X", "Y", "Z"]:
        b.append(x)
print(set(b))

