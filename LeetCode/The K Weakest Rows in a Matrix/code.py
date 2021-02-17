# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3641/


from collections import defaultdict

class Solution:
    def kWeakestRows(self,mat, k):
        
        data = dict()
        idx = 0
        for sub in mat:
            data[idx] = sub.count(1)
            idx += 1
        sor = list(data.values())        
        sor.sort()
        lookup = defaultdict(list)
        for i in sor:
            lookup[i]
        # print(lookup)
        for key,val in data.items():
            lookup[val].append(key)
        
        res = []
        for va in lookup.values():
            res.extend(va)
        
        return res[:k]




obj = Solution()
mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
k = 3
print(obj.kWeakestRows(mat,k))