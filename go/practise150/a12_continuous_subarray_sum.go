package practise150

// You are given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

// A good subarray is a subarray where:

//     its length is at least two, and
//     the sum of the elements of the subarray is a multiple of k.

func ContinuosSubarraySum(nums []int, k int) bool {
	remainderMap := make(map[int]int)
	sum := 0

	for i, n := range nums {
		sum += n
		r := sum % k

		if val, ok := remainderMap[r]; !ok {
			remainderMap[r] = i
		} else if i-val > 1 {
			return true
		}
	}
	return false
}
