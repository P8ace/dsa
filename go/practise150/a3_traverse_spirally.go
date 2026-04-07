package practise150

// Given a 2D array of size m*n traverse it in spiral order. 

func TraverseSpirally(matrix [][]int) []int{
	top, left := 0,0
	bottom, right := len(matrix)-1, len(matrix[0])-1
	result := make([]int,0)
	
	for left <= right && top <= bottom {
		
		for i := left; i <= right; i++ {
			result = append(result, matrix[top][i])
		}
		top++
		
		for i:= top; i <= bottom; i++ {
			result = append(result, matrix[i][right])
		}
		right--
		
		for i:=right; i >= left; i-- {
			result = append(result, matrix[bottom][i])
		}
		bottom--
		
		for i:= bottom; i >= top; i-- {
			result = append(result, matrix[i][left])
		}
		left++
			
	}
	return result
}