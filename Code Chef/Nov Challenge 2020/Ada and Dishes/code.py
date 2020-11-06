for _ in range(int(input())):
    N = int(input())
    A = list(map(int,input().split()))

    if N == 1:
        print(A[0])
    if N == 2:
        print(max(A[0],A[1]))
    if N == 3:
        print(min(max(A[0]+A[1],A[2]),max(A[0]+A[2],A[1]),max(A[1]+A[2],A[0])))
    if N == 4:
        print(min(max(A[0],A[1]+A[2]+A[3]),max(A[1],A[0]+A[2]+A[3]),max(A[2],A[0]+A[1]+A[3]),max(A[3],A[1]+A[2]+A[0]),max(A[0]+A[1],A[2]+A[3]),max(A[0]+A[2],A[1]+A[3]),max(A[0]+A[3],A[1]+A[2])))
