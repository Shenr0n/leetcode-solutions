class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        kDict = {}
        kFreq = []
        result = []
        for val in nums:
            kDict[val] = kDict.get(val,0)+1

        for i in kDict.keys():
            heappush(kFreq, (-kDict[i],i))

        while k>0:
            result.append(heappop(kFreq)[1])
            k -= 1

        return result
