from random import randint
n = 25
while n > 0:
    num = randint(0, 1000)
    num2 = randint(10, 5000)
    print("Сумма и произведение чисел", num, "и", num2)
    print("Сумма:", num+num2)
    print("Произведение", num*num2)
    n -= 2
