//nlogn Time Complexity

func topKFrequent(nums []int, k int) []int {
    last := len(nums)
    var freq = make(map[int]int)
    var kNums []int

//Add the numbers and their frequencies in a map
    for i:=0; i<last; i++ {
        if _, ok := freq[nums[i]]; ok {
            freq[nums[i]]++
        } else {
            freq[nums[i]] = 1
        }
    }

//Array of unique keys from the map, i.e. unique elements from the nums array
    for key := range freq {
        kNums = append(kNums, key)
    }

//Sorting the unique keys array using SliceStable in descending order of value from map
    sort.SliceStable(kNums, func(i, j int) bool {
        return freq[kNums[i]]>freq[kNums[j]]})
    
//Return a Slice with k most frequent elements
    return kNums[:k]
    
}
