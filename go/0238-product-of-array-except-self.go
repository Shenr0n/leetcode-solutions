func productExceptSelf(nums []int) []int {
    length := len(nums)
    prod := make([]int, length) 
    right := 1
    prod[0] = 1
    for i:= 1; i<length; i++ {
        prod[i] = prod[i-1]*nums[i-1]
    }
    for i:=length-1; i>=0; i-- {
        prod[i] = prod[i]*right
        right = right*nums[i]
    }
    return prod
}
