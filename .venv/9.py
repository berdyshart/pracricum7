N,K,R = map(int,input().split())
if N >= R:
    print(1)
else:
    r = (100+K)/100
    for i in range(2, 10**10):
        dl = N*r-N
        N*=r
        if N >= R:
            print(i)
            break
