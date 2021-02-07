# https://www.geeksforgeeks.org/sum-of-bit-differences-among-all-pairs/

class Solution():
    def sumBitDiff(self,arr, n):
        ans = 0 
        for i in range(0, 32):  
            count = 0
            for j in range(0, n): 
                if ( (arr[j] & (1 << i)) ): 
                    count+= 1
            ans += (count * (n - count) * 2); 
        return ans 


# arr = [1, 3, 5] 
# n = len(arr)
# obj = Solution()

# print(obj.sumBitDiff(arr, n)) 

"""
HINT = Find some mathematical formula using information of total number of set bits in all the numbers at a particular ith bit position.

"""
#Back-end complete function Template for Python 3

class Solution:
    def sumBitDiff(self, arr, n): 
        ans = 0  # Initialize result 
      
        # traverse over all bits 
        for i in range(0, 32): 
          
            # count number of elements with i'th bit set 
            count = 0
            for j in range(0,n): 
                if ( (arr[j] & (1 << i)) ): 
                    count+=1
      
            # Add "count * (n - count) * 2" to the answer 
            ans += (count * (n - count) * 2); 
          
        return ans