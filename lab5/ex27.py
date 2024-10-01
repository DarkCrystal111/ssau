n = 0
nums = []
while n <= 40:
    if n % 2 != 0:
        nums.append(n**2)
    n += 1
print("Сумма квадратов 40 нечетных чисел равна:", sum(nums))