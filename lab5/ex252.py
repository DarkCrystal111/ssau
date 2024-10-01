from random import randint
from math import prod
n = 25
nums = []
while n > 0:
    nums.append(randint(0, 100))
    n -= 1
print("Числа", *nums)
print("Сумма чисел:", sum(nums))
print("Произведение чисел:", prod(nums))
