class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        dp = [[float("infinity") for j in range(m)] for i in range(n)]
        for i in range(n-1,-1,-1):
            if i == n-1:
                dp[i][m-1] = grid[i][m-1] 
            else:
                dp[i][m-1] = grid[i][m-1] + dp[i+1][m-1]
        
        for i in range(m-1,-1,-1):
            if i == m-1:
                dp[n-1][i] = grid[n-1][i] 
            else:
                dp[n-1][i] = grid[n-1][i] + dp[n-1][i+1]
        
        for i in range(n-2,-1,-1):
            for j in range(m-2,-1,-1):
                dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])
        return dp[0][0]  