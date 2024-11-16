a = input("Введите строку: ")
if "".join(reversed(list(a))) == a:
    print("Строка палиндром")
else:
    print("Строка не палиндром")
