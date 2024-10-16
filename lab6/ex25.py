from math import ceil
y = 40
count = 0
total = 0
for x in range(1, 11):
    y = y + y / 100 * 5
    total += y
print("В книге", ceil(total), "страниц")