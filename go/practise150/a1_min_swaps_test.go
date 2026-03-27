package practise150

import (
	"fmt"
	"testing"
)

func Test_min_swaps(t *testing.T) {
	test_cases := []struct {
		input    []int
		expected int
	}{
		{
			input:    []int{2, 8, 5, 4},
			expected: 4,
		},
		{
			input:    []int{10, 19, 6, 5, 3},
			expected: 2,
		},
		{
			input:    []int{1, 3, 4, 5, 6},
			expected: 4,
		},
	}

	for i, test_case := range test_cases {
		t.Run(fmt.Sprintf("Test_case_no:%d", i+1), func(t *testing.T) {
			actual := min_swaps(test_case.input)
			if actual != test_case.expected {
				t.Errorf("Input: %v, Expected: %d, Actual: %d", test_case.input, test_case.expected, actual)
			}
		})
	}
}
