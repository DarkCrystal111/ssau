from random import randint
from math import prod
n = int(input("n: "))
numbers = []
for x in range(0, n+1):
    numbers.append(randint(1, 100))
print("Все числа:", *numbers)
print("Сумма чисел:", sum(numbers))
print("Произведение чисел:", prod(numbers))