count = 0
number = 1000
while number < 10000:
    if number % 3 == 0:
        count += 1
    number += 1
print("Всего", count, "четырехзначных чисел, кратных трем.")