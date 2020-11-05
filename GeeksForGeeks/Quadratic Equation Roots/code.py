'''
Problem Statement : https://practice.geeksforgeeks.org/problems/quadratic-equation-roots/1
'''

class Solution:
    def quadraticRoots(self,a,b,c):
        Helpee = lambda a,b,c:((b**2) - (4 * a * c))
        tr = Helpee(a,b,c)
        if tr<0:
            return [-1]
        else:
            firstR = int((-1*(b) + ((tr)**(1/2)))//(2*a))
            SecondR = int((-1*(b) - ((tr)**(1/2)))//(2*a))
            return sorted([firstR,SecondR],reverse=True)
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        abc=[int(x) for x in input().strip().split()]
        a=abc[0]
        b=abc[1]
        c=abc[2]
        ob = Solution()
        ans = ob.quadraticRoots(a,b,c)
        if len(ans)==1 and ans[0]==-1:
            print("Imaginary")
        else:
            for i in range(len(ans)):
                print(ans[i], end=" ")
            print()

# } Driver Code Ends