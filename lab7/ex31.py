from random import randint
for x in range(0, 11):
    a = randint(-10, 10)
    if a == 0:
        break
    elif a < 0:
        continue
    else:
        print(pow(a, 1/2))
