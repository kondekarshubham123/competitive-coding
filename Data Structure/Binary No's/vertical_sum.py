'''
Quetion : Sum of Binary and Decimal Numbers

You have given integer N your task is too determine sum of all numbers from 1 to N without selecting any decimal
no directly you have required to convert the decimal number into binary numbers and then add the same.

Example
N = 3
Dec  Bin
1    01
2   +10
3   +11
-------
     22

Constarints 
1 <= N <= 10**18

since the ans can be large determine required ans modulo 10**9 + 7
'''
def myFinaladd(ll):
    ans = ''
    mod = 10**9 + 7
    for nu in range(len(ll)):
        pnt = len(ll) -1 - nu
        if pnt == 0:
            ans = str(ll[pnt]) + ans
            break
        R = ll[pnt]%10
        D = ll[pnt]//10
        ll[pnt-1] += D
        ans = str(R) + ans
    
    return int(ans)%mod

def getSetBitsFromzeroToN(N):
    two = 2
    ans = 0
    n = N
    track = []
    while(n):
        tc = (N//two)*(two>>1)
        if((N&(two-1)) > (two>>1)-1):
            tc = (N&(two-1)) - (two>>1)+1 
        track.append(tc)
        two <<= 1
        n >>= 1
    # print(track[::-1])
    return myFinaladd(track)

print(getSetBitsFromzeroToN(900000000000))