class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n,m = len(heights),len(heights[0])
        res = []
        pacific = set()
        atlantic = set()
        def dfs(i,j,visit,prev):
            if i<0 or j<0 or i == n or j ==m or (i,j) in visit or heights[i][j] < prev:
                return
            visit.add((i,j))
            dfs(i+1,j,visit,heights[i][j])
            dfs(i-1,j,visit,heights[i][j])
            dfs(i,j+1,visit,heights[i][j])
            dfs(i,j-1,visit,heights[i][j])
        
        for i in range(n):
            dfs(i,0,pacific,heights[i][0])
            dfs(i,m-1,atlantic,heights[i][m-1])
        for j in range(m):
            dfs(0,j,pacific,heights[0][j])
            dfs(n-1,j,atlantic,heights[n-1][j])
        
        for s in pacific:
            if s in atlantic:
                res.append(list(s))
        return res
