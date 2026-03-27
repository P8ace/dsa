package practise150

import "slices"

// Given an integer array nums and an integer k, return the k most frequent elements within the array.
// Eg:
//     Input: nums = [1,2,2,3,3,3], k = 2

//     Output: [2,3]

//     Input: nums = [7,7], k = 1

//     Output: [7]

//     Input: nums = [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9], k = 4
//     Output: [5, 11, 7, 10]
//     Explanation: Frequency of 5 is 3, frequency of 11 is 2, frequency of 7 is 2, and frequency of rest is 1  but 10 is largest .

func top_k_frequenct_elements(nums []int, k int) []int {
	count_map := make(map[int]int)
	for _, n := range nums {
		count_map[n]++
	}

	frequency_array := make([][]int, len(nums)+1)
	for key, value := range count_map {
		frequency_array[value] = append(frequency_array[value], key)
	}

	final := []int{}
	for i := len(frequency_array) - 1; i > 0; i-- {
		cloned := make([]int, len(frequency_array[i]))
		copy(cloned, frequency_array[i])
		slices.SortFunc(cloned, func(a, b int) int {
			if a < b {
				return 1
			} else if a > b {
				return -1
			}
			return 0
		})
		for _, val := range cloned {
			final = append(final, val)
			if len(final) == k {
				return final
			}
		}
	}
	return []int{}
}
