a = int(input("Стипендия: "))
b = int(input("Траты в месяц: "))
n = 1
current = b
while n < 10:
    b = b+b/100*3
    current += b
    n += 1
print("Нужно попросить", round(current-(a*10)), "рублей.")