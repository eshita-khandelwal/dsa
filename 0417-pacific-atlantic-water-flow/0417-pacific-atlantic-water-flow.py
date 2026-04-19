class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac,alt = set(),set()
        ROW,COL = len(heights),len(heights[0])
        def dfs(r,c,visit,prevHeight):
            if r<0 or c<0 or c==COL or r==ROW or (r,c) in visit or heights[r][c]<prevHeight:
                return 
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])

        for i in range(ROW):
            # pac.add((i,0))
            # alt.add((i,COL-1))
            dfs(i,0,pac,heights[i][0])
            dfs(i,COL-1,alt,heights[i][COL-1])
        
        for j in range(COL):
            # pac.add((0,j))
            # alt.add((ROW-1,j))
            dfs(0,j,pac,heights[0][j])
            dfs(ROW-1,j,alt,heights[ROW-1][j])
        
        res = []
        for i,j in pac:
            if (i,j) in alt:
                res.append([i,j])
        return res
