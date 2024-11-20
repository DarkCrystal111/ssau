n = int(input("Введите число n: "))
x = int(input("Введите число x: "))
val = 0
for k in range(1, n+1):
    for m in range(k, n+1):
        val += (x+k)/m
print(val)
