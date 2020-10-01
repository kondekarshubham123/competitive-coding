FunLL = lambda lis:lis[0][0]==lis[1][1]
FunRR = lambda lis:lis[0][1]==lis[1][0]



for tt in range(int(input())):
    n,m = map(int,input().split())
    LL,RR,LR = False,False,False
    arrays = [[list(map(int,input().split()))]+[list(map(int,input().split()))] for _ in range(n)]
    if m%2!=0:
        print("NO")
        continue
    
    for array in arrays:
        if FunLL(array) and FunRR(array):
            LR = 1
            break
        elif FunRR(array):
            RR = True
            break
    print("YES" if (LR==1 or RR == 1) else "NO")
    