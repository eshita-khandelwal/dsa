class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
      
        def dfs(i,j):
            if i<0 or i>=n or j<0 or j>=m or board[i][j]!='O':
                return 
            
            board[i][j] = 'T'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        #convert all border and border connected cells from O --> T
        for r in range(n):
            for c in range(m):
                if board[r][c] == 'O' and (r==0 or c==0 or r==n-1 or c==m-1):
                    dfs(r,c)
        
        #convert all o's to X
        for r in range(n):
            for c in range(m):
                if board[r][c]=='O':
                    board[r][c] = 'X'
        
        #convert all T's to O
        for r in range(n):
            for c in range(m):
                if board[r][c]=='T':
                    board[r][c] = 'O'
        
        