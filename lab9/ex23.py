a = input("Введите строку: ")
b = "".join([x*2 if x != " " else x for x in a])
print(b)
