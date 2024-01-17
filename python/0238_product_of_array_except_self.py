class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pLeft = [0]*(len(nums))
        pRight = [0]*(len(nums))

        pLeft[0] = 1
        pRight[-1] = 1

        for i in range(1,len(nums)):
            pLeft[i] = pLeft[i-1]*nums[i-1]
        
        for i in range(len(nums)-2,-1,-1):
            pRight[i] = pRight[i+1]*nums[i+1]

        for i in range(0,len(nums)):
            pLeft[i] = pLeft[i]*pRight[i]
        
        return pLeft
