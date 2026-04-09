package practise150

import (
	"fmt"
	"testing"
)

func TestContinuousSubarraySum(t *testing.T) {
	test_cases := []struct {
		input    []int
		k        int
		expected bool
	}{
		{
			input:    []int{23, 2, 4, 6, 7},
			k:        6,
			expected: true,
		},
		{
			input:    []int{23, 2, 6, 4, 7},
			k:        6,
			expected: true,
		},
		{
			input:    []int{23, 2, 6, 4, 7},
			k:        13,
			expected: false,
		},
	}
	for idx, tc := range test_cases {
		t.Run(fmt.Sprintf("Test_case_no:%d", idx+1), func(t *testing.T) {
			actual := ContinuosSubarraySum(tc.input, tc.k)
			if actual != tc.expected {
				t.Errorf("Testing Continuous subarray sum divisible by k. Input: %v, K: %d, Expected: %v, Actual: %v.\n",
					tc.input, tc.k, tc.expected, actual)
			}
		})
	}
}
