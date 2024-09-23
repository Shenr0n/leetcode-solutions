class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        maxL = 0
        maxR = 0
        left = 0
        right = len(height) - 1

        while left < right:
            maxL = max(maxL, height[left])
            maxR = max(maxR, height[right])
            tempwater = 0
            
            if maxL < maxR:
                tempwater = maxL - height[left]
                left += 1
            else:
                tempwater = maxR - height[right]
                right -= 1

            if tempwater > 0:
                water += tempwater
                
        return water

                

