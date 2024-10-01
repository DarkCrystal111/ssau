from math import ceil
y = 40
count = 0
while count < 10:
    y += y/100*5
    count += 1
print("В книге", ceil(y), "страниц")