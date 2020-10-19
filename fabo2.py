lookup = {0:0,1:1}

N = int(input())

if N in lookup.keys():
    print(lookup[N])
else:

    for i in range(2,N+1):
        lookup[i] = lookup[i-1]+lookup[i-2]
    
    # print(lookup)
    print(lookup[N])