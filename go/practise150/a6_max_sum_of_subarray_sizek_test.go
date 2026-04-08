package practise150

import (
	"fmt"
	"testing"
)

func TestMaxSumofSubarraySizek(t *testing.T) {
	test_cases := []struct {
		input    []int
		k        int
		expected int
	}{
		{
			input:    []int{100, 200, 300, 400},
			k:        2,
			expected: 700,
		},
		{
			input:    []int{4, 2, 10, 23, 3, 1, 0, 20},
			k:        4,
			expected: 39,
		},
		{
			input:    []int{100, 200, 300, 400},
			k:        1,
			expected: 400,
		},
	}
	for idx, test_case := range test_cases {
		t.Run(fmt.Sprintf("test_case_no:%d", idx+1), func(t *testing.T) {
			actual := MaxSumofsubarray(test_case.input, test_case.k)
			if actual != test_case.expected {
				t.Errorf("Testing Max sum of subarray of size k method 1. Input: %v, K: %d. Expected: %d, Actual: %d.", test_case.input, test_case.k, test_case.expected, actual)
			}
		})
	}
	for idx, test_case := range test_cases {
		t.Run(fmt.Sprintf("test_case_no:%d", idx+1), func(t *testing.T) {
			actual := MaxSumofsubarray2(test_case.input, test_case.k)
			if actual != test_case.expected {
				t.Errorf("Testing Max sum of subarray of size k method 2. Input: %v, K: %d. Expected: %d, Actual: %d.", test_case.input, test_case.k, test_case.expected, actual)
			}
		})
	}
}
