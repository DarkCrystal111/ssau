a = input("Введите числа множества A через пробел: ")
b = input("Введите числа множества B через пробел: ")
A = {}
B = {}
A.update(a.split())
B.update(b.split())
print("Отличающиеся числа:", A.symmetric_difference_update(B))
A &= B
print("Совпадающие числа во множествах:", sort(A))
