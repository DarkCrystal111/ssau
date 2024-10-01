hours = 1
ceils = 1
while hours <= 24:
    if hours % 3 == 0:
        ceils *= 2
        print("В", hours, "часов", ceils, "амеб")
    hours += 1