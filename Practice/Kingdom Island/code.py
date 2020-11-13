class Solution(object):
    islandCount = 0
    def numIslands(self, grid):
        ans = []
        for r,row in enumerate(grid):
            for c,col in enumerate(row):
                if grid[r][c] == '1':
                    self.removeNeighbors(r,c,grid)
                    ans.append(self.islandCount)
                    self.islandCount = 0
        return max(ans)

    def removeNeighbors(self, r ,c, grid):
        grid[r][c] = 0 
        # print(grid)
        self.islandCount+=1   
        if r+1 < len(grid) and grid[r+1][c] == '1':
            self.removeNeighbors(r+1,c,grid)
        if c+1 < len(grid[0]) and grid[r][c+1] == '1':
            self.removeNeighbors(r,c+1,grid)    
        if r-1 >= 0 and grid[r-1][c] == '1':
            self.removeNeighbors(r-1,c,grid)
        if c-1 >= 0 and grid[r][c-1] == '1':
            self.removeNeighbors(r,c-1,grid)


N,M = list(map(int,input().split()))
grid = [input().split() for _ in range(N)]
check =  Solution()
print(check.numIslands(grid))