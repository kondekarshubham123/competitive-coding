for tt in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))

    for i in range(1,n):
        if (i!=n-1):
            if a[i-1]==a[i]:
                a[i] = b[i]
        else:
            if a[0]!=b[i] and b[i] != a[i-1]:
                a[i]=b[i]
            elif a[0]!=c[i] and c[i] != a[i-1]:
                a[i]=c[i]
                     
    print(*a)
        
