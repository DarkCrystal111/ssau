n = 7
nums = []
while n <= 37:
    if n % 2 != 0:
        nums.append(n**3)
    n += 1
print("Сумма кубов нечетных чисел от 7 до 37 равна:", sum(nums))