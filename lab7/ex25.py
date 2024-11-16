n = int(input("n: "))
m = int(input("m: "))
flag = 0
for x in range(0, m):
    if flag == 0:
        print("-"*n)
        flag = 1
    else:
        print("+"*n)
        flag = 0

