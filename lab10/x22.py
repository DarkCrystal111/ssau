a = input("Введите последовательность: ").split()
b = []
for x in a:
    if x.isdigit() and 0 <= int(x) < 6 or x.isalpha() and len(x) < 2:
        b.append(x)
print(set(b))

