package practise150

//
// Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
// You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

// Eg:
//     nums = [3,4,5,6], target = 7

//     Output: [0,1]

//

func two_sum(nums []int, target int) []int {
	unvisited := make(map[int]int)

	for i, num := range nums {
		diff := target - num
		if val, ok := unvisited[diff]; ok {
			return []int{val, i}
		} else {
			unvisited[num] = i
		}
	}
	return []int{}
}
