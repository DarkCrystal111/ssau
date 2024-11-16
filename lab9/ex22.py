while True:
    a = input("Введите слово: ")
    if a.endswith("с") or a.endswith("С"):
        print("Ваше слово:", a)
        continue
    break
