package practise150

import (
	"fmt"
	"slices"
)

// Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
// where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

// The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

func ThreeSum(nums []int) [][]int {
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
	result := [][]int{}
	for i, _ := range nums {
		if nums[i] > 0 {
			break
		}
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		j := i+1
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
				result = append(result, []int{nums[i], nums[j], nums[k]})
				j++
				k--
				for j < k && nums[j] == nums[j-1] {
					j++
				}
			}
		}
	}
	return result
}
