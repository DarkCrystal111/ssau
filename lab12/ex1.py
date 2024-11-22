m = int(input("m: "))
n = int(input("n: "))
matrix = []
for x in range(1, m+1):
    t = []
    for i in range(1,n+1):
        t.append(input(f"m{x}, n{i}: "))
    matrix.append(t)
for e, x in enumerate(matrix):
    if e % 2 == 0:
        print(*x)
    else:
        print(*reversed(x))
