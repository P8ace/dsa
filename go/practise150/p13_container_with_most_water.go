package practise150

// You are given an integer array heights where heights[i] represents the height of the ithith bar.
// You may choose any two bars to form a container. Return the maximum amount of water a container can store.
// Eg:
//     Input: height = [1,7,2,5,4,7,3,6]  
//     Output: 36    
//     Here distance between 7(i=1) and 6(i=7) is 6. and min between the two is 6, so the answer is 6*6


func MaxAmountOfWater(heights []int) int {
	i := 0
	j := len(heights) - 1
	maxWater := 0
	
	for i < j {
		minHeight := min(heights[i], heights[j])
		water := (j - i) * minHeight
		maxWater = max(maxWater, water)
		if heights[i] >  heights[j] {
			j-- 
		} else {
			i++
		}
	}
	return maxWater
}