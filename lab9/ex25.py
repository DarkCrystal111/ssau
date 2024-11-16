a = input("Введите строку: ")
b = []
for x in a.replace(" ", ""):
    if x not in b:
        b.append(x)
print("".join(b))
