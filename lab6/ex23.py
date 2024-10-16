x = int(input("x: "))
km = 0
for n in range(1, 8):
    km += x + km // 10
print("Спортсмен пробежал", km, "км.")
