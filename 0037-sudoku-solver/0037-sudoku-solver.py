class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #use backtracking here
        n = len(board)
        m = len(board[0])
        row = collections.defaultdict(list)
        col = collections.defaultdict(list)
        b = collections.defaultdict(list)
        for i in range(n):
            for j in range(m):
                if board[i][j]!='.':
                    num = int(board[i][j])
                    row[i].append(num)
                    col[j].append(num)
                    b[(i//3,j//3)].append(num)
        
        def backtrack(r,c):
            nonlocal solved
            if r == 9:
                solved = True
                return
            new_r = r + (c+1)//9
            new_c = (c+1)%9
            if board[r][c]!='.':
                backtrack(new_r,new_c)
            else:
                for i in range(1,10):
                    if (i not in row[r] ) and (i not in col[c] ) and (i not in b[(r//3,c//3)]):
                        row[r].append(i)
                        col[c].append(i)
                        b[(r//3,c//3)].append(i)
                        board[r][c] = str(i)
                        backtrack(new_r,new_c)
                        if not solved:
                            row[r].remove(i)
                            col[c].remove(i)
                            b[(r//3,c//3)].remove(i)
                            board[r][c] = '.'
        solved = False
        backtrack(0,0)
                    
