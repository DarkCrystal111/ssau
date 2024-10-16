a = int(input("Стипендия: "))
b = int(input("Траты в месяц: "))

money = b
for x in range(2, 11):
    b = b+b/100*3
    money += b
print("Нужно попросить", round(money-(a*10)), "рублей.")
