class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        op = [1]*length
        left, right = 1, 1

        for i in range(length):
            op[i] = left
            left *= nums[i]
        
        for i in range(length-1,-1,-1):
            op[i] *= right
            right *= nums[i]
        return op