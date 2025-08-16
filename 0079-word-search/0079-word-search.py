class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n,m = len(board),len(board[0])
        seen = set()
        def dfs(i,j,k):
            if k == len(word):
                return True
            if j<0 or i<0 or i == n or j == m or board[i][j]!=word[k] or (i,j) in seen:
                return False
            
            if board[i][j] == word[k]:
                seen.add((i,j))
                found = dfs(i+1,j,k+1) or dfs(i-1,j,k+1) or dfs(i,j+1,k+1) or dfs(i,j-1,k+1)
                if found:
                    return True
                seen.remove((i,j))
                return found
        
        for i in range(n):
            for j in range(m):
                if dfs(i,j,0):
                    return True
        
        return False
