package practise150

// Given an array of integers numbers that is sorted in non-decreasing order.
// Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number "target" and index1 < index2.
// Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

func TwoSumIndexed1(nums []int, target int) []int{
	hashset := make(map[int]int)
	
	for idx, n := range nums {
		diff := target - n
		if val, ok := hashset[diff]; !ok {
			hashset[n] = idx
		} else if n < diff {
			return []int{idx +1, val+1}
		} else {
			return []int{val+1, idx+1}
		}
	}
	return nil
}

func TwoSumIndexed1WithTwoPointers(nums []int, target int) []int {
	l := 0
	r := len(nums) -1
	
	for l < r {
		sum := nums[l] + nums[r]
		if sum < target {
			l++
		} else if sum > target {
			r--
		} else {
			return []int{l + 1, r + 1}
		}
	}
	return nil	
}