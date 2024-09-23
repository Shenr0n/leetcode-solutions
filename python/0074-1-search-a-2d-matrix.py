# O(log m + log n)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left = 0
        right = len(matrix)-1
        row = -1

        while left <= right:
            mid = left+(right-left)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                row = mid
                left = mid + 1
            else:
                right = mid - 1

        if row == -1:
            return False

        left = 0
        right = len(matrix[row])-1

        while left <= right:
            mid = left+(right-left)//2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
