package practise150

import (
	"fmt"
	"testing"
)

func TestMinSizeSubarraySum(t *testing.T) {
	test_cases := []struct {
		input    []int
		target   int
		expected int
	}{
		{
			input:    []int{2, 1, 5, 1, 5, 3},
			target:   10,
			expected: 3,
		},
		{
			input:    []int{1, 2, 1},
			target:   5,
			expected: 0,
		},
	}
	for idx, tc := range test_cases {
		t.Run(fmt.Sprintf("test_case_no:%d", idx+1), func(t *testing.T) {
			actual := MinSubarraySum(tc.input, tc.target)
			if actual != tc.expected {
				t.Errorf("Testing min size subarray sum >= k. Input: %v, Target: %d, Expected: %d, Actual :%d.\n", tc.input, tc.target, tc.expected, actual)
			}
		})
	}
}
