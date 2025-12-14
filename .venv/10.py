s = float(input())
prev = 0.0
n = 0
while s != 0.0:
    prev, s = s, float(input())
    if prev > s:
        n+=1
print(n-1)