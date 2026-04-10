package practise150

import (
	"fmt"
	"testing"
)

func TestMaximumSubarray(t *testing.T) {
	test_cases := []struct {
		input    []int
		expected int
	}{
		{
			input:    []int{2, -3, 4, -2, 2, 1, -1, 4},
			expected: 8,
		},
		{
			input:    []int{-1},
			expected: -1,
		},
	}
	for idx, tc := range test_cases {
		t.Run(fmt.Sprintf("Test_case_no:%d", idx+1), func(t *testing.T) {
			actual := MaximumSubarray(tc.input)
			if actual != tc.expected {
				t.Errorf("Testing maximum subarray. Input: %v, Expected: %d, Actual: %d.\n", tc.input, tc.expected, actual)
			}
		})
	}
}
