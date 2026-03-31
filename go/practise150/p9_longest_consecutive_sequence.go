package practise150

// Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

// A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.
// The elements do not have to be consecutive in the original array.

// Eg:
//     Input: nums = [2,20,4,10,3,4,5]
//     Output: 4

func LongestConsecutiveSequence(nums []int) int {
	hashmap := make(map[int]struct{})

	for _, n := range nums {
		hashmap[n] = struct{}{}
	}

	count := 0

	for n, _ := range hashmap {
		if _, ok := hashmap[n-1]; !ok {
			length := 1
			for {
				if _, ok := hashmap[n+length]; ok {
					length += 1
				} else {
					break
				}

			}
			count = max(count, length)
		}
	}

	return count
}
