count = 1
hours = 1
for x in range(1, 25):
    if x % 3 == 0:
        count *= 2
        print(count, "амеб будет через", hours, "часа")
    hours += 1
