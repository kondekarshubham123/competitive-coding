def convertToWave(A,N):
    A.sort()
    low = A[::2]
    high = A[1::2]
    ans = []
    for i,j in list(zip(high,low)):
        ans.extend([i,j])
    if len(ans) != N:
        ans+=[A[-1]]
    for i in range(N):
        A[i] = ans[i]


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().split()]
        convertToWave(A,N)
        for i in A:
            print(i,end=" ")
        
        
        print()
        
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends