n = int(input("Введите число n: "))
val = 0
for i in range(n+1):
    for j in range(i, n+1):
        val += (n+j)/(2*i+j+1)
print(val)
