n = int(input("Введите число n: "))
val = 0
for i in range(n+1):
    for j in range(i+1):
        print((i, j))
        val += (3*i-j)/2
print(val)
