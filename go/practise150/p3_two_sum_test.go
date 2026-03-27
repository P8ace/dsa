package practise150

import (
	"fmt"
	"slices"
	"testing"
)

func Test_two_sum(t *testing.T) {
	test_cases := []struct {
		input    []int
		target   int
		expected []int
	}{
		{
			input:    []int{3, 4, 5, 6},
			target:   7,
			expected: []int{0, 1},
		},
		{
			input:    []int{4, 5, 6},
			target:   10,
			expected: []int{0, 2},
		},
		{
			input:    []int{5, 5},
			target:   10,
			expected: []int{0, 1},
		},
	}

	for i, test_case := range test_cases {
		t.Run(fmt.Sprintf("Testcase no:%d", i+1), func(t *testing.T) {
			actual := two_sum(test_case.input, test_case.target)
			if !slices.Equal(actual, test_case.expected) {
				t.Errorf("Input: %v, Target: %v, Expected:  %v, Actual: %v", test_case.input, test_case.target, test_case.expected, actual)
			}
		})
	}
}
