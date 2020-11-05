#User function Template for python3

#Complete this function
def leaders(A,N):
    if N == 1:
        return [A]
    
    A = A[::-1]
    ans = [A[0]]
    ma = A[0]

    for i in range(1,N):
        if ma<=A[i]:
            ma = A[i]
            ans.append(A[i])
    return ans[::-1]


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        
        A=leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends