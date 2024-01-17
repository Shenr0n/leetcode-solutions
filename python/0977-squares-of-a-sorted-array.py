class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        revSqSorted = []
        left = 0
        right = len(nums)-1
        
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                revSqSorted.append(nums[left]**2)
                left += 1
            else:
                revSqSorted.append(nums[right]**2)
                right -=1

        return revSqSorted[::-1]
