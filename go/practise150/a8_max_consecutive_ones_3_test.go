package practise150

import (
	"fmt"
	"testing"
)

func TestMaxConsecutiveOnes3(t *testing.T) {
	test_cases := []struct {
		input    []int
		k        int
		expected int
	}{
		{
			input:    []int{1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0},
			k:        2,
			expected: 6,
		},
		{
			input:    []int{0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1},
			k:        3,
			expected: 10,
		},
	}
	for idx, tc := range test_cases {
		t.Run(fmt.Sprintf("Test_Case_No:%d", idx+1), func(t *testing.T) {
			actual := MaxConsecutiveOnes3(tc.input, tc.k)
			if actual != tc.expected {
				t.Errorf("Testing Maximum consecutive ones. Input: %v, K: %d, Expected: %d, Actual: %d.\n", tc.input, tc.k, tc.expected, actual)
			}
		})
	}

}
