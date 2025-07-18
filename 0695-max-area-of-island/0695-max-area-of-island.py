class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        res = 0
        def dfs(i,j):
            if i<0 or j<0 or i==n or j==m or grid[i][j]!=1:
                return 0
            grid[i][j] = -1
            return 1 + dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1)
        
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    ans = dfs(r,c)
                    res = max(res,ans)
        return res
            