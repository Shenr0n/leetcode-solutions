/*
Sum of three values
Given an array of integers, nums, and an integer value, target, determine if there are any three
integers in nums whose sum is equal to the target, that is, nums[i] + nums[j] + nums[k] ==
target. Return TRUE if three such integers exist in the array. Otherwise, return FALSE.

Note: A valid triplet consists of elements with distinct indexes. This means, for the triplet
nums[i], nums[j], and nums[k], i != j, j!= k, i !=k

Constraints

3<= nums.length <= 500
-10^3 <= nums[i] <= 10^3
-10^3 <= target <= 10^3

Example:
nums = [2, 1, 6, 4, 8, 20]
target = 31
Output: false

nums = [1, -3, 1]
target = -1
Output: true

*/
package main
import "sort"

func findSumOfThree(nums []int, target int) bool {
	// Replace this placeholder return statement with your code

  left, right, sum := 0,0,0

  sort.Sort(sort.IntSlice(nums))

  for i:=0; i<len(nums)-2; i++ {
    left = i+1
    right = len(nums)-1

    for left < right {
      sum = nums[i]+nums[left]+nums[right]
      if sum == target {
        return true
      } else if sum < target {
        left++
      } else {
        right--
      }
    }
  }
  return false
}
