class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = len(nums)
        numset = set()

        for i in range(len(nums)):
            numset.add(nums[i])
        
        maxSeq = 0
        for num in numset:
            seq = 0
            if (num-1) in numset:
                continue
            temp = num
            while temp in numset:
                seq += 1
                temp += 1
            maxSeq = max(seq, maxSeq)
        return maxSeq
            
