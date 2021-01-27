class Solution:
    def smallestpositive(self, array, n): 
        # print(array,n)
        if all(list(map(lambda x:x==1,array))):
            return n+1

        array.sort()
        # print(array)
        if array[0] > 1:
            return 1

        res = 1
        for i in range (0, n ): 
            if arr[i] <= res: 
                res = res + arr[i] 
            else: 
                break
        return res 
            





obj = Solution()
arr = [1,1, 11, 16]
print(obj.smallestpositive(arr,3))