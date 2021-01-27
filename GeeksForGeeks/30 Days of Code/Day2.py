'''
Nth Natural Number

Given a positive integer N. You have to find Nth natural number after removing all the 
numbers containing digit 9 .

Input:
N = 8
Output:
8
Explanation:
After removing natural numbers which contains
digit 9, first 8 numbers are 1,2,3,4,5,6,7,8
and 8th number is 8.
'''

class Solution:
    def findNth(self,N):
        #code here
        ans = 0
        i = 0
        while N:
            ans += ((10**i)*(N%9))
            N //= 9
            i += 1
        return ans

# for i in range(0,int(input()))
#     N = int(input())
#     obj = Solution()
#     s = obj.findNth(N)
#     print(s)