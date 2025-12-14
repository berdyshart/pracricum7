ans = int(input())
num = 1
for i in range(1, 13):
    num*=2
    if i in [5, 7, 12]:
        if num == ans:
            print("верно")
            break
else:
    print("nеверно")
