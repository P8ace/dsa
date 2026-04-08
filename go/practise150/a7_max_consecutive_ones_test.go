package practise150

import (
	"fmt"
	"testing"
)

func TestMaxConsecutiveOnes(t *testing.T) {
	test_cases := []struct {
		input    []int
		expected int
	}{
		{
			input:    []int{1, 1, 0, 1, 1, 1},
			expected: 3,
		},
		{
			input:    []int{1, 0, 1, 1, 0, 1},
			expected: 2,
		},
	}
	for idx, tc := range test_cases {
		t.Run(fmt.Sprintf("Test_Case_No:%d", idx+1), func(t *testing.T) {
			actual := MaxConsecutiveOnes(tc.input)
			if actual != tc.expected {
				t.Errorf("Testing Maximum consecutive ones. Input: %v, Expected: %d, Actual: %d.\n", tc.input, tc.expected, actual)
			}
		})
	}

}
