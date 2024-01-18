func replaceElements(arr []int) []int {
    i := len(arr)-1
    rightMax := -1
    for i >= 0 {
        temp := arr[i]
        arr[i] = rightMax
            rightMax = max(temp,rightMax)
        i--
    }
    return arr
}
