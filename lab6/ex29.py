nums = []
for x in range(41):
    if x % 2 != 0:
        nums.append(x**2)
print("Сумма квадратов 40 нечетных чисел равна:", sum(nums))