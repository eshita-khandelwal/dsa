class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        def bfs(grid,i,j):
            if i<0 or j<0 or i == len(grid) or j == len(grid[0]) or (i,j) in visit or grid[i][j]=="0":
                return 0
            
            visit.add((i,j))
            bfs(grid,i,j-1)
            bfs(grid,i,j+1)
            bfs(grid,i-1,j)
            bfs(grid,i+1,j)


        islandCnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visit:
                    bfs(grid,i,j)
                    islandCnt+=1
        return islandCnt
        