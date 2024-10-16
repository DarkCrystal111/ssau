n = 0
nums = []
for x in range(31):
    if x % 2 == 0:
        nums.append(x**2)
print("Сумма квадратов 30 четных чисел равна:", sum(nums))