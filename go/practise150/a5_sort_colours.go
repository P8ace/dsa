package practise150

// You are given an array nums consisting of n elements where each element is an integer representing a color:

//     0 represents red
//     1 represents white
//     2 represents blue

// Your task is to sort the array in-place such that elements of the same color are grouped together and
// arranged in the order: red (0), white (1), and then blue (2).

func sortColours(nums []int) {
	countMap := make(map[int]int)
	for _, n := range nums {
		countMap[n]++
	}
	idx := 0
	for i := 0; i <= 2; i++ {
		for countMap[i] > 0 {
			countMap[i]--
			nums[idx] = i
			idx++
		}
	}
}
