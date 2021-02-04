# Repeated String Match
"""
Given two strings A and B, find the minimum number of times A has to be repeated such that B becomes a 
substring of the repeated A. If B cannot be a substring of A no matter how many times it is repeated, 
return -1.

Example 1:

Input: A = "abcd", B = "cdabcdab"
Output: 3
Explanation: After repeating A three times, 
we get "abcdabcdabcd".

Example 2:

Input: A = "aa", B = "a"
Output: 1
Explanation: B is already a substring of A.

Your Task:  
You don't need to read input or print anything. Complete the function repeatedStringMatch() which takes strings A and B as input parameters and returns the minimum number of operations to complete the task. If it is not possible then return -1.

Expected Time Complexity: O(|A| * |B|)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ |A|, |B| ≤ 103
"""


# import math
## Wrong coz it will increament A badly
class Solution:
    def repeatedStringMatch(self, A, B):
        # code here
        res = 1
        count = len(B)//len(A)+1
        for i in range(count):
            if B in A:
                return res
            else:
                A += A
                res += 1
        else:
            return -1

import math
class Solution:
    def repeatedStringMatch(self, A, B):
        # code here
        m = math.ceil(len(B)/len(A))
        
        if B in A*m:
            return m
        elif B in A*(m+1):
            return m+1
        else:
            return -1





obj = Solution()
A = "abcd"
B = "cdabcdab"
print(obj.repeatedStringMatch(A,B))




"""
HINT :
Let count = B.length() / A.length().
Now check whether B is a substring of A*count or A*(count+1)

"""
## Ans
#Back-end complete function Template for Python 3

class Solution:
    def repeatedStringMatch(self, A,B):
        S=A
        ret=1
        
        while len(S)<len(B):
            S+=A
            ret+=1
        
        if B in S:
            return ret
        
        if B in S+A:
            return ret+1
        
        return -1