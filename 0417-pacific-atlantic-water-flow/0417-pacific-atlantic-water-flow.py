class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac,alt = set(),set()
        n,m = len(heights),len(heights[0])

        def dfs(r,c,visit,prev):
            if r<0 or r==n or c<0 or c==m or (r,c) in visit or heights[r][c] < prev:
                return 
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])


        for r in range(n):
            dfs(r,0,pac,heights[r][0])
            dfs(r,m-1,alt,heights[r][m-1])
        
        for c in range(m):
            dfs(0,c,pac,heights[0][c])
            dfs(n-1,c,alt,heights[n-1][c])
        
        res = []

        for val in pac:
            if val in alt:
                res.append(val)
        
        return res