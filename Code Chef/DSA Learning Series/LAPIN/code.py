from collections import Counter
for _ in range(int(input())):
    inp = list(input())
    ll = len(inp)
    idx = 0
    EVEN,ODD = False,False
    if ll%2==0:
        EVEN = True
        idx = ll//2
    else:
        ODD = True
        idx = (ll//2)+1
    if EVEN:
        firH  = Counter(inp[:idx])
        secH  = Counter(inp[idx:])
    else:
        # print(inp)
        # print(inp[:idx-1])
        # print(inp[idx:])
        firH  = Counter(inp[:idx-1])
        secH  = Counter(inp[idx:])


    if firH == secH:
        print("YES")
    else:
        print("NO")
