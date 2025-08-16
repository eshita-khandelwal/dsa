class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        q = deque()
        seen = set()
        fcount = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fcount +=1

        minutes = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                #grid[r][c] = 0
                if r+1 < n and grid[r+1][c]==1:
                    q.append((r+1,c))
                    grid[r+1][c] = 2
                    fcount -=1
                if r-1>=0 and grid[r-1][c]==1:
                    q.append((r-1,c))
                    grid[r-1][c] = 2
                    fcount -=1
                if c+1 < m and grid[r][c+1]==1:
                    q.append((r,c+1))
                    grid[r][c+1] = 2
                    fcount -=1
                if c-1>=0 and grid[r][c-1]==1:
                    q.append((r,c-1))
                    grid[r][c-1] = 2
                    fcount -=1
            if q:
                minutes +=1
        return minutes if fcount == 0 else -1
                



