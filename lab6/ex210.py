nums = []
for x in range(6, 37):
    if x % 2 == 0:
        nums.append(x**3)
print("Сумма кубов четных чисел от 6 до 36 равна:", sum(nums))