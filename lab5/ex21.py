count = 0
x = 10
while count < 7:
    x += x/100*10
    count += 1
print("Спортсмен пробежал:", round(x, 3), "км.")
