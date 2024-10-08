class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = row*col - 1

        while left <= right:
            mid = left+(right-left)//2
            temprow = mid//col
            tempcol = mid%col
            if matrix[temprow][tempcol] == target:
                return True
            elif matrix[temprow][tempcol] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
