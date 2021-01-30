"""
Spiral Matrix

Given a matrix of size N x M. 
You have to find the Kth element which will obtain while traversing the matrix spirally 
starting from the top-left corner of the matrix.

Input: 
N = 3, M = 3, K = 4
A[] = {{1, 2, 3}, 
       {4, 5, 6}, 
       {7, 8, 9}}
Output: 
6
Explanation: Spiral traversal of matrix: 
{1, 2, 3, 6, 9, 8, 7, 4, 5}. Fourth element
is 6.


Input: 
N = 2, M = 2, K = 2 
A[] = {{1, 2},
       {3, 4}} 
Output: 
2
Explanation: Spiral traversal of matrix: 
{1, 2, 4, 3}. Second element is 2.

Your Task:  
You don't need to read input or print anything. 
Complete the function findK() which takes the matrix A[ ][ ], 
number of rows N, number of columns M, and integer K as input parameters and 
returns the Kth element in the spiral traversal of the matrix.

Expected Time Complexity: O(N*M)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ K ≤ N*M ≤ 106
"""
"""
#User function Template for python3

# You are required to complete this fucntion
# Function should return an integer
class Solution:
    def mycall(self,a,n,m,k,i,j,t,xi,yi,zi,wi,dire="x"):
        if k == t:
            return a[i][j],wi
        t += 1

        if dire == "x":
            j += 1
            if j == yi:
                xi += 1
                return self.mycall(a,n,m,k,i,j,t,xi,yi,zi,wi,dire="y")
            else:
                return self.mycall(a,n,m,k,i,j,t,xi,yi,zi,wi,dire="x")
        
        elif dire == "y":
            i += 1
            if i == zi:
                yi -= 1
                return self.mycall(a,n,m,k,i,j,t,xi,yi,zi,wi,dire="z")
            else:
                return self.mycall(a,n,m,k,i,j,t,xi,yi,zi,wi,dire="y")

        elif dire == "z":
            j -= 1
            if j == wi:
                zi -= 1
                return self.mycall(a,n,m,k,i,j,t,xi,yi,zi,wi,dire="w")
            else:
                return self.mycall(a,n,m,k,i,j,t,xi,yi,zi,wi,dire="z")

        elif dire == "w":
            i -=  1
            if i == xi:
                wi += 1
                return self.mycall(a,n,m,k,i,j,t,xi,yi,zi,wi,dire="x")
            else:
                return self.mycall(a,n,m,k,i,j,t,xi,yi,zi,wi,dire="w")



    def findK(self, a, n, m, k):
        xi = 0
        yi = n-1
        zi = m-1
        wi = 0
        return self.mycall(a,n,m,k-1,0,0,0,xi,yi,zi,wi)

obj = Solution()
print(obj.findK(a,N,M,K))
"""

# Submitted
class Solution():

    def findK(self,A, n, m, k): 

        if (n < 1 or m < 1): 
            return -1

        '''....If element is in outermost ring ....'''
        ''' Element is in first row '''
        if (k <= m): 
            return A[0][k - 1] 

        ''' Element is in last column '''
        if (k <= (m + n - 1)): 
            return A[(k - m)][m - 1] 

        ''' Element is in last row '''
        if (k <= (m + n - 1 + m - 1)): 
            return A[n - 1][m - 1 - (k - (m + n - 1))] 

        ''' Element is in first column '''
        if (k <= (m + n - 1 + m - 1 + n - 2)): 
            return A[n - 1 - (k - (m + n - 1 + m - 1))][0] 


        '''....If element is NOT in outermost ring ....'''
        ''' Recursion for sub-matrix. &A[1][1] is 
        address to next inside sub matrix.'''
        A.pop(0) 
        [j.pop(0) for j in A] 
        return self.findK(A, n - 2, m - 2, k - (2 * n + 2 * m - 4)) 


## Suggested
class Solution:
    def findK(self, a, n, m, k):
        top = 0
        left = 0
        right = m-1;
        bottom = n-1;
        dir =0;
        count=0;
        while(top<=bottom and left<=right):
            if(dir==0):
                for i in range(left, right+1):
                    k -= 1
                    if k == 0:
                        return (a[top][i])
                top += 1
                dir=1
                    
            if(dir==1):
                for i in range(top, bottom+1):
                    k -= 1
                    if k == 0:
                        return (a[i][right])
                right -= 1
                dir=2
            if(dir==2):
                for i in range(right, left - 1, -1):
                    k -= 1
                    if k == 0:
                        return (a[bottom][i])
                bottom -= 1
                dir=3
            if(dir==3):
                for i in range(bottom, top - 1, -1):
                    k -= 1
                    if k == 0:
                        return (a[i][left])
                left += 1
                dir=0