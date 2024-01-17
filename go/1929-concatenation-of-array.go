func getConcatenation(nums []int) []int {
    l := len(nums)
    nums2 := make([]int, l*2)

    for i:=0; i<l; i++ {
        nums2[i], nums2[i+l] = nums[i],nums[i]
    }
    return nums2

    /*
    return append(nums,nums...)
    */
}
