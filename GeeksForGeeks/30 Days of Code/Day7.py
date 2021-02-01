"""
Valid Pair Sum

Given an array of size N, find the number of distinct pairs 
{a[i], a[j]} (i != j) in the array with their sum greater than 0.

Input: N = 3, a[] = {3, -2, 1}
Output: 2
Explanation: {3, -2}, {3, 1} are two 
possible pairs.

Input: N = 4, a[] = {-1, -1, -1, 0}
Output: 0
Explanation: There are no possible pairs.


Your Task:  
You don't need to read input or print anything. 
Complete the function ValidPair() which takes the array a[ ] and 
size of array N as input parameters and returns the count of such pairs.

Expected Time Complexity: O(N * Log(N))
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 105 
-104  ≤ a[i] ≤ 104
"""
from itertools import combinations
class Solution1:
    
    def ValidPair(self, a, n): 
    	# Your code goes here
        cnt = 0
        for i,j in combinations(a,2):
            if i+j > 0:
                cnt += 1
        return cnt


class Solution:
    
    def ValidPair(self, a, n):
        ans = 0
        p,q = 0,n-1
        a.sort()

        while(p<q):
            if a[p]+a[q] > 0:
                ans += q-p
                q-=1
            else:
                p+=1
        return ans 	    
	
obj = Solution()
n = 3
a = [3, -2, 1]
print(obj.ValidPair(a,n))

# Suggested
#Back-end complete function Template for Python 3

from bisect import bisect_left as lower_bound 
class Solution:
    def ValidPair(self, a, n): 
    	a = sorted(a) 
    	ans = 0
    	for i in range(n): 
    		if (a[i] <= 0): 
    			continue
    		# search for first element >= (-a[i] + 1)
    		j = lower_bound(a,-a[i] + 1) 
    		ans += i - j 
    	return ans 