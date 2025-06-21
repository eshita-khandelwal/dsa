class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashRow = {} #0->[],1->[]
        hashCol={}
        hashGrid={}
        for i in range(0,9):
            hashRow[i] = hashRow.get(i,[])
            for j in range(0,9):
                if board[i][j] == ".":
                    continue
                hashCol[j] = hashCol.get(j,[])
                if board[i][j] not in hashRow[i]:
                    hashRow[i].append(board[i][j])
                elif board[i][j] in hashRow[i]:
                    return False
                if board[i][j] not in hashCol[j]:
                    hashCol[j].append(board[i][j])
                elif board[i][j] in hashCol[j]:
                    return False
                hashGrid[(i//3,j//3)] = hashGrid.get((i//3,j//3),[])
                if board[i][j] not in hashGrid[(i//3,j//3)]:
                    hashGrid[(i//3,j//3)].append(board[i][j])
                elif board[i][j] in hashGrid[(i//3,j//3)]:
                    return False
        return True
                