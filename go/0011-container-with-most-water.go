func Min(x, y int) int {
    if x < y{
        return x
    }
    return y
}

func maxArea(height []int) int {
    var left, maxWater, tempWater int
    right := len(height)-1
    
    for left<right {
        tempWater = Min(height[right],height[left])*(right-left)
        if tempWater > maxWater {
            maxWater = tempWater
        }
        if height[left] < height[right] {
            left++
        } else {
            right--
        }
    }
    return maxWater
}
