class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh,time = 0,0
        ROWS,COLS = len(grid),len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append([i,j])
        
        while q and fresh>0:
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    if r+dr < 0 or r+dr >= ROWS or c+dc<0 or dc+c>= COLS  or grid[r+dr][c+dc]!=1:
                        continue
                    grid[r+dr][c+dc]=2
                    q.append([r+dr,c+dc])
                    fresh-=1
            time+=1
        
        return -1 if fresh!=0 else time
                    