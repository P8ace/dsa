package practise150

// Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

// Example:
//     Input: nums = [1, 2, 3, 3]
    
//     Output: true

func contains_duplicate(nums []int) bool{
	unvisited := make(map[int]struct{})
	
	for _, item := range nums {
		if _, ok := unvisited[item]; !ok {
			unvisited[item] = struct{}{}
		} else {
			return true
		}
	}
	return false
}