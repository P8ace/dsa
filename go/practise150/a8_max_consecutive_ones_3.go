package practise150

// Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

func MaxConsecutiveOnes3(nums []int, k int) int {
	i, j := 0, 0
	count := 0

	for j < len(nums) {
		if nums[j] == 0 {
			k--
		}
		for k < 0 {
			if nums[i] == 0 {
				k++
			}
			i++
		}
		count = max(count, j-i+1)
		j++
	}
	return count
}
