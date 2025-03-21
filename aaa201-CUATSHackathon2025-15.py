class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L1 = 0
        L2 = 0
        R1 = len(matrix[0]) - 1
        R2 = len(matrix) - 1

        while L2 <= R2:
            M2 = (L2 + R2) // 2
            if target > matrix[M2][-1]:
                L2 = M2 + 1
            elif target < matrix[M2][0]:
                R2 = M2 - 1
            else:
                break

        row = matrix[M2]
        while L1 <= R1:
            M1 = (L1 + R1) // 2
            if target > row[M1]:
                L1 = M1 + 1
            elif target < row[M1]:
                R1 = M1 -1
            else:
                return True

        return False

        
