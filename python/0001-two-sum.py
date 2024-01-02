class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        twoSumHash = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in twoSumHash:
                return [twoSumHash[diff], i]
            twoSumHash[n] = i
