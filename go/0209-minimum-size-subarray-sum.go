func minSubArrayLen(target int, nums []int) int {
    var tempSum, tempCount, left int
    var minCount = len(nums)+1
    l := len(nums)

    for right:=0; right < l; right++ {
        if nums[right] == target {
            return 1
        }
        if (tempSum + nums[right]) >= target {
            if tempCount < minCount{
                minCount = tempCount
            }
            tempSum = tempSum - nums[left]
            left++
            right--
            tempCount--
        } else {
            tempCount++
            tempSum = tempSum + nums[right]
        } 
    }
    if minCount > len(nums){
        return 0
    }
    return minCount+1
}
