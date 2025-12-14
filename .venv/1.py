c = 0
num=100
while num < 1000:
    if num % 17 == 0:
        print(num, end=" ")
        c+=1
        num+=17
    else:
        num+=1
print()
print(c)
