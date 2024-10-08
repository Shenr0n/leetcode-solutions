class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        op = right

        while left <= right:
            mid = left+(right-left)//2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile/mid)
            if hours <= h:
                op = min(op, mid)
                right = mid - 1
            else:
                left = mid + 1
        return op