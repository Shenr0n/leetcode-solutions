func minimumDifference(nums []int, k int) int {
    sort.Ints(nums)
    minVal := math.MaxInt64
    left := 0
    right := k-1

    for right<=len(nums)-1 {
        if nums[right]-nums[left] <= minVal {
            minVal = nums[right]-nums[left]
        }
        left++
        right++
    }
    return minVal
}
