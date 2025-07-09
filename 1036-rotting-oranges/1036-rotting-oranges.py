class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time,fresh = 0,0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] ==2:
                    q.append([i,j])
                if grid[i][j] == 1:
                    fresh +=1
        
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                if r>=0 and c+1<col and grid[r][c+1] == 1:
                    q.append([r,c+1])
                    grid[r][c+1] = 2
                    fresh -=1
                if r>=0 and c-1>=0 and grid[r][c-1] == 1:
                    q.append([r,c-1])
                    grid[r][c-1] = 2
                    fresh -=1
                if r+1<row and c<col and grid[r+1][c] == 1:
                    q.append([r+1,c])
                    grid[r+1][c] = 2
                    fresh -=1
                if r-1>=0 and c<col and grid[r-1][c] == 1:
                    q.append([r-1,c])
                    grid[r-1][c] = 2
                    fresh -=1
            time+=1
        
        return time if fresh == 0 else -1
            