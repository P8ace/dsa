package practise150

import (
	"fmt"
	"testing"
)

func TestSubarrayProductLessthanK(t *testing.T) {
	test_cases := []struct {
		input    []int
		k        int
		expected int
	}{
		{
			input:    []int{10, 5, 2, 6},
			k:        100,
			expected: 8,
		},
		{
			input:    []int{1, 2, 3},
			k:        0,
			expected: 0,
		},
		{
			input:    []int{1, 1, 1},
			k:        1,
			expected: 0,
		},
	}
	for idx, test_case := range test_cases {
		t.Run(fmt.Sprintf("Test_Case_No:%d", idx+1), func(t *testing.T) {
			actual := Nosubarrayproductlessthank(test_case.input, test_case.k)
			if actual != test_case.expected {
				t.Errorf("Testing No of subarray with product less than k. Input: %v, K: %d, Expected: %d, Actual: %d. \n", test_case.input, test_case.k, test_case.expected, actual)
			}
		})
	}
}
