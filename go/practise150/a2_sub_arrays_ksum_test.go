package practise150

import (
	"fmt"
	"testing"
)

func TestNoofSubarrays(t *testing.T) {
	test_cases := []struct {
		input    []int
		k        int
		expected int
	}{
		{
			input:    []int{1, 1, 1},
			k:        2,
			expected: 2,
		},
		{
			input:    []int{1, 3, 5},
			k:        0,
			expected: 0,
		},
		{
			input:    []int{1, 2, 3},
			k:        3,
			expected: 2,
		},
		{
			input:    []int{4, 4, 4, 4, 4, 4},
			k:        4,
			expected: 6,
		},
		{
			input:    []int{1, 2, 1},
			k:        5,
			expected: 0,
		},
		{
			input:    []int{10, 2, -2, -20, 10},
			k:        -10,
			expected: 3,
		},
		{
			input:    []int{9, 4, 20, 3, 10, 5},
			k:        33,
			expected: 2,
		},
	}
	for idx, test_case := range test_cases {
		t.Run(fmt.Sprintf("test_case_no:%d", idx+1), func(t *testing.T) {
			actual := NoofSubarraysofsumK(test_case.input, test_case.k)
			if actual != test_case.expected {
				t.Errorf("Testing no of sub array of sum K. Input: %v, K: %d, Expected: %d, Actual: %d.", test_case.input, test_case.k, test_case.expected, actual)
			}
		})
	}
	for idx, test_case := range test_cases {
		t.Run(fmt.Sprintf("2nd method test_case_no:%d", idx+1), func(t *testing.T) {
			actual := NoofSubarraysofsumK(test_case.input, test_case.k)
			if actual != test_case.expected {
				t.Errorf("Testing no of sub array of sum K. Input: %v, K: %d, Expected: %d, Actual: %d.", test_case.input, test_case.k, test_case.expected, actual)
			}
		})
	}
}
