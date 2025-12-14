s = input()
for i in range(len(s)):
    if (i-2)%3 == 0:
        print(s[i], end="")
