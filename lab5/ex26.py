n = 0
nums = []
while n <= 30:
    if n % 2 == 0:
        nums.append(n**2)
    n += 1
print("Сумма квадратов 30 четных чисел равна:", sum(nums))