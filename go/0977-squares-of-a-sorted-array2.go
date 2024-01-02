func sortedSquares(nums []int) []int {

    l := len(nums)-1
    result := make([] int, (l+1))

    for i,j := 0,l; l>=0; l--{
        if nums[i]<0 && -nums[i] >= nums[j]{
            result[l] = nums[i]*nums[i]
            i++
        } else {
            result[l] = nums[j]*nums[j]
            j--
        }
    }
    return result
}
