n = int(input("Введите число n: "))
val = 0
for k in range(1, n+1):
    for m in range(1, n+1):
        val += n/(2*k+m)
print(val)
