count = 0
for x in range(1000, 10000):
    if x % 3 == 0:
        count += 1
print("Всего", count, "четырехзначных чисел, кратных трем.")