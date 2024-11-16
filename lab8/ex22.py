a = input("Введите строку: ")
count = 0
for x in a.split():
    if x[0] == "b":
        count += 1
print(count, "слов, начинающихся с b")
