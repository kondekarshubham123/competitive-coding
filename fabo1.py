lookup = [0,1]

N = int(input())

if N in [0,1]:
    print(lookup[N])
else:

    for i in range(2,N+1):
        lookup.append(lookup[i-1]+lookup[i-2])
    
    print(lookup)
    print(lookup[N])