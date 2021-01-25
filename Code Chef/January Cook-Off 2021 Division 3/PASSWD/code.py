import re
t = int(input())

while t:
    myst = input()
    ll = len(myst) - 1
    lc,uc,di,sc = [False]*4
    cnt = 0
    for idx,i in enumerate(myst):
        if i in 'qwertyuiopasdfghjklzxcvbnm':
            lc = True
        if idx != 0 and idx != ll and  i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            uc = True
        if idx != 0 and idx != ll and i in '1234567890':
            di = True
        if idx != 0 and idx != ll and (i in [  '@', '#', '%', '&', '?' ]):
            sc = True
        cnt += 1
    if all([lc,uc,di,sc]) and cnt > 9:
        print("YES")
    else:
        print("NO")

    t-=1