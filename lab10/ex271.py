a = input("Введите последовательность: ").split()
b = []
for x in a:
    if x in [",", ".", "-", ";", ":", ")", "(", "'", '"'] or x.isalpha() and x.upper() in ["E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]:
        b.append(x)
print(set(b))

