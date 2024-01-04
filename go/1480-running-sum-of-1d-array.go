func runningSum(nums []int) []int {
    last := len(nums) - 1

    for i:=1;i<=last;i++{
        nums[i] += nums[i-1]
    }
    return nums
}
