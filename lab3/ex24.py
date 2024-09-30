m = int(input("m: "))
n = int(input("n: "))
if m == n:
    n, m = (0, 0)
else:
    n = max(n, m)
    m = n
print("n: ", n)
print("m: ", m)

