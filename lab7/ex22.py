n = int(input("Введите число n: "))
val = 0
for i in range(n+1):
    for j in range(n+1):
        val += pow(i, 2)-2*j
print(val)
