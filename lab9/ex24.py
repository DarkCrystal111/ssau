a = input("Введите строку: ")
b = ""
for x in a.split():
 if len(x) > len(b):
  b = x
print(b)
