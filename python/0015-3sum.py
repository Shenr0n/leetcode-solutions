class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        op = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1

            while left < right:
                sum3 = num + nums[left] + nums[right]
                    
                if sum3 < 0:
                    left += 1
                elif sum3 > 0:
                    right -= 1
                else:
                    op.append([num, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        return op