package practise150

// Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
// A subarray is a contiguous non-empty sequence of elements within an array.

func NoofSubarraysofsumK(nums []int, k int) int {
	// Use prefix sum with hashmap when you need to match a sum of k and count sub arrays
	prefixSum := 0
	count := 0
	sumMap := map[int]int{
		0: 1,
	}

	for i := 0; i < len(nums); i++ {
		prefixSum += nums[i]
		diff := prefixSum - k
		if val, ok := sumMap[diff]; ok {
			count += val
		}
		sumMap[prefixSum]++
	}
	return count
}

func NoofSubarraysofsumK2(nums []int, k int) int {
	// Use prefix sum with hashmap when you need to match a sum of k and count sub arrays
	prefixSum := 0
	count := 0
	sumMap := make(map[int]int)

	for i := 0; i < len(nums); i++ {
		prefixSum += nums[i]
		if prefixSum == k {
			count++
		}
		diff := prefixSum - k
		if val, ok := sumMap[diff]; ok {
			count += val
		}
		sumMap[prefixSum]++
	}
	return count
}
