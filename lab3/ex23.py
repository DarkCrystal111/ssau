x = int(input("x: "))
y = int(input("y: "))
if x < y:
    x1 = x
    x = (x+y)/2
    y = (x1*y)*2
else:
    x1 = x
    x = (x1*y)*2
    y = (x1+y)/2
print("x: ", x)
print("y: ", y)
