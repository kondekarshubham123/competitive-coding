class Solution:
    def prank(self, a, n): 
        #code here
        arr = a.copy()
        arr = [arr[i] for i in arr]
        for i in range(n):
            a[i] = arr[i]
