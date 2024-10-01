a = int(input("Стипендия: "))
b = int(input("Траты в месяц: "))
n = 1
current = 0
while n < 10:
    current += b + b/100*3
    n += 1
print("Нужно попросить", round(current-(a*10)), "рублей.")
