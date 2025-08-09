class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        n,m = len(grid),len(grid[0])
        def dfs(r,c):
            if r<0 or c<0 or r==n or c==m or grid[r][c] != 1:
                return 0
            grid[r][c] = -1
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c-1) + dfs(r,c+1) 
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    res = max(res,dfs(i,j))
        return res