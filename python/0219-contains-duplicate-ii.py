class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicateSet = set()
        left = 0

        for right in range(len(nums)):
            if abs(left - right) > k:
                duplicateSet.remove(nums[left])
                left += 1
            if nums[right] in duplicateSet:
                return True
            else:
                duplicateSet.add(nums[right])
        return False
