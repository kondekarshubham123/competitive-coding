def main(N,K,Arr):

    for i in range(N-1):
        pos = i

        for j in range(i+1,N):
            if (j-i > K):
                break
            
            if (Arr[j] <  Arr[pos]):
                pos = j
        
        for j in range(pos,i,-1):
            Arr[j],Arr[j-1] = Arr[j-1],Arr[j]
        K -= pos - i

for _ in range(int(input())):
    N,K = list(map(int,input().split()))
    Arr = list(map(int,input().split()))
    main(N,K,Arr)
    print(*Arr)