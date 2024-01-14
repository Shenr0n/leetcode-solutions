class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicateMap = {}

        for value in nums:
            if value in duplicateMap.keys():
                return True
            else:
                duplicateMap[value] = 1
        return False