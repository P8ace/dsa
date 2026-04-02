package practise150

// You are given an array of non-negative integers height which represent an elevation map.
// Each value height[i] represents the height of a bar, which has a width of 1.
// Return the maximum area of water that can be trapped between the bars.

func TrapRain(heights []int) int {
	i, j := 0, len(heights)-1
	leftMax, rightMax, MaxWater := 0, 0, 0

	for i < j {
		if heights[i] < heights[j] {
			leftMax = max(leftMax, heights[i])
			MaxWater += leftMax - heights[i]
			i++
		} else {
			rightMax = max(rightMax, heights[j])
			MaxWater += rightMax - heights[j]
			j--
		}
	}
	return MaxWater
}
