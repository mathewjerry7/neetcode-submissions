class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        columns = len(matrix[0])

        top = 0
        bottom = rows - 1 
        target_row = 0

        while top <= bottom:
            matrix_mid = (top + bottom) // 2

            if target > matrix[matrix_mid][columns - 1]:
                top = matrix_mid+1
            elif target < matrix[matrix_mid][0]:
                bottom = matrix_mid - 1
            else:
                target_row = matrix_mid
                break
        
        left, right = 0, columns - 1

        while left <= right:
            mid = (left + right) // 2

            if target == matrix[target_row][mid]:
                return True
            elif target > matrix[target_row][mid]:
                left = mid+1
            else:
                right = mid - 1

        return False

        