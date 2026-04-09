package practise150

import (
	"fmt"
	"testing"
)

func TestSubarraySumDivisiblebyK(t *testing.T) {
	test_cases := []struct {
		input    []int
		k        int
		expected int
	}{
		{
			input:    []int{4, 5, 0, -2, -3, 1},
			k:        5,
			expected: 7,
		},
		{
			input:    []int{5},
			k:        9,
			expected: 0,
		},
	}
	for idx, tc := range test_cases {
		t.Run(fmt.Sprintf("Test_case_no:%d", idx+1), func(t *testing.T) {
			actual := SubarraySumDivisblebyK(tc.input, tc.k)
			if actual != tc.expected {
				t.Errorf("Testing subarray sum divisible by K. Input: %v, K: %d, Expected: %d, Actual: %d,\n",
					tc.input, tc.k, tc.expected, actual)
			}
		})
	}
}
