from math import ceil

for t in range(1,int(input())+1):
    N,X = map(int,input().split())
    A = list(map(int,input().split()))
    #print(A)
    Arr = []
    for _ in range(N):
        Arr.append((ceil(A[_]/X),_+1))
    Arr.sort()
    ans = [idx for ele,idx in Arr]
        

    print("Case #{0}: {1}".format(t," ".join(list(map(str,ans)))))