package practise150

// You are given a binary array nums, return the maximum number of consecutive 1's in the array.

func MaxConsecutiveOnes(nums []int) int {
	j := 0
	count := 0
	maxCount := 0

	for j < len(nums) {
		if nums[j] == 1 {
			count++
			j++
		} else if nums[j] == 0 {
			count = 0
			j++
		}
		maxCount = max(maxCount, count)
	}
	return maxCount
}
// func MaxConsecutiveOnesMethod2(nums []int) int {
// 	i, j := 0, 0
// 	count := 0

// 	for j < len(nums) {
// 		count = max(count, j-i+1)
// 		if nums[j] == 1 {
// 			j++
// 		} else if nums[j] == 0 {
// 			j++
// 			i = j
// 		}
// 	}
// 	return count
// }
