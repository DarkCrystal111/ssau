m = int(input("m: "))
n = int(input("n: "))
matrix = []
for x in range(1, m+1):
    t = []
    for i in range(1,n+1):
        t.append(int(input(f"m{x}, n{i}: ")))
    matrix.append(t)
nums = 0
for x in range(m):
    for i in range(n):
        if i != x and i >= 0:
            nums += matrix[x][i]
print(nums)

