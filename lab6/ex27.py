nums = []
for x in range(7, 38):
    if x % 2 != 0:
        nums.append(x**3)
print("Сумма кубов нечетных чисел от 7 до 37 равна:", sum(nums))