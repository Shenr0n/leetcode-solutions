class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        op = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                left = j+1
                right = len(nums)-1

                while left < right:
                    sum3 = nums[j] + nums[left]+ nums[right]

                    if a + sum3 < target:
                        left += 1
                    elif a + sum3 > target:
                        right -= 1
                    else:
                        op.append([a, nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1

        return op