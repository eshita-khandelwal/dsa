class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = collections.defaultdict(list)
        row = collections.defaultdict(list)
        subbox = collections.defaultdict(list)


        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in col[j]:
                    return False
                col[j].append(board[i][j])
                if board[i][j] in row[i]:
                    return False
                row[i].append(board[i][j])
                if board[i][j] in subbox[(i//3,j//3)]:
                    return False
                subbox[(i//3,j//3)].append(board[i][j])
        return True
                


        