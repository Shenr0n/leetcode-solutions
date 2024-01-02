func reverseArray(nums []int) []int{
    length := len(nums)
    for i, j := 0, length-1; i < j; i, j = i+1, j-1 {
        nums[i], nums[j] = nums[j], nums[i]
    }
    return nums
}

func sortedSquares(nums []int) []int {
    var result []int

    left := 0
    right := len(nums)-1

    for left <= right{
        if math.Abs(float64(nums[left])) > math.Abs(float64(nums[right])){
            result = append(result, nums[left]*nums[left])
            left++
        } else {
            result = append(result, nums[right]*nums[right])
            right--
        }
    }
    return reverseArray(result)
}
