from math import sqrt

k = int(input("k: "))
for x in range(0, k+1):
    print("Корень числа", x, "равен", sqrt(x), "а куб равен", pow(x, 3))