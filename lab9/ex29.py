a = input("Введите строку: ").replace(" ","")
if "".join(reversed(list(a))) == a:
    print("Строка палиндром")
else:
    print("Строка не палиндром")
