package practise150

// Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

func SubarraySumDivisblebyK(nums []int, k int) int {
	remainderMap := make(map[int]int)
	remainderMap[0] = 1
	sum := 0
	count := 0

	for _, n := range nums {
		sum += n
		r := (sum%k + k) % k
		count += remainderMap[r]
		remainderMap[r]++
	}
	return count
}
