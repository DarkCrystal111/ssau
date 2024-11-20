n = int(input("Введите число n: "))
val = 0
for i in range(n+1):
    for j in range(i, n+1):
        val += (3*i-j)/2
print(val)
