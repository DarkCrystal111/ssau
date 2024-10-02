from math import ceil
y = 40
count = 0
total = 0
while count < 10:
    y = y + y/100*5
    total += y
    count += 1
print("В книге", ceil(total), "страниц")