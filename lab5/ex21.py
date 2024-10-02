count = 0
x = int(input("Введите x: "))
km = 0
while count < 7:
    km += x + km //10
    count += 1
print("Спортсмен пробежал:", round(km, 3), "км.")
