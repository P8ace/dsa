package practise150

import (
	"fmt"
	"slices"
)

// Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
// where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

// The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

func ThreeSum(nums []int) []int {
	// nums[i] + nums[j] + nums[k] == 0
	// nums[j] + nums[k] == -nums[i]

	slices.SortFunc(nums, func(a, b int) int {
		if a < b {
			return -1
		} else if a > b {
			return 1
		} else {
			return 0
		}
	})
	fmt.Println("Sorted", nums)
	for i, _ := range nums {
		j := 0
		k := len(nums) - 1
		for j < k {
			if i == j {
				i++
			} else if i == k {
				k--
			}
			sum := nums[j] + nums[k]
			if sum < -nums[i] {
				j++
			} else if sum > -nums[i] {
				k--
			} else {
				fmt.Println("i,j,k", i, j, k)
				return []int{nums[i], nums[j], nums[k]}
			}
		}
	}
	return nil
}
