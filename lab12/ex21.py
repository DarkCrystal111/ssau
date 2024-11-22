m = int(input("m: "))
n = int(input("n: "))
matrix = []
for x in range(1, m+1):
    t = []
    for i in range(1,n+1):
        t.append(int(input(f"m{x}, n{i}: ")))
    matrix.append(t)
nums = []
for x in range(n):
    t = 0
    for i in range(m):
        t += matrix[i][x]
    nums.append(t)
for e, x in enumerate(nums):
    print("Сумма", e+1, "столбца равна", x)
