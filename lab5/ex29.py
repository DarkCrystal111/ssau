count = 2 # т.к. 5 уже задана, а + 1 count только в конце
number = 5
step = 4
while number <= 324:
    number += number + step
    count += 1

print("Нужно взять", count, "слагаемых")