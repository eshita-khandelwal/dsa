class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col = len(matrix),len(matrix[0])
        top = 0
        bottom = row-1
        while top <= bottom:
            m = (top+bottom)//2
            if target > matrix[m][-1]:
                top = m + 1
            elif target < matrix[m][0]:
                bottom = m -1
            else:
                break
        if not (top<=bottom):
            return False
        top = (top+bottom)//2
        l, r = 0,col-1
        while l<=r:
            m = (l+r)//2
            if matrix[top][m] > target:
                r = m -1
            elif matrix[top][m] < target:
                l = m +1
            else:
                return True
        return False
