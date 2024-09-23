import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        op = []
        #freq = defaultdict(int)
        freq={}

        for num in nums:
            #freq[num] += 1
            freq[num] = 1 + freq.get(num, 0)

        for key, val in freq.items():
            heapq.heappush(heap, (-val, key))
        
        while(len(op) < k):
            op.append(heapq.heappop(heap)[1])
        
        return op
