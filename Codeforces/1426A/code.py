from math import ceil

for tt in range(int(input())):
    Pttya , NoAppa = map(int,input().split())
    if Pttya in [1,2]:
        print(1)
    else:
        Pttya-=2
        print(ceil(Pttya/NoAppa+1))