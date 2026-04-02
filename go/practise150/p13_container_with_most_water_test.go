package practise150

import (
	"fmt"
	"testing"
)

func TestMaxAmountOfWater(t *testing.T) {
	type TestCases struct {
		input    []int
		expected int
	}

	test_cases := []TestCases{
		{
			input:    []int{1, 7, 2, 5, 4, 7, 3, 6},
			expected: 36,
		},
		{
			input:    []int{12, 2, 2},
			expected: 4,
		},
		{
			input:    []int{1, 5, 4, 3},
			expected: 6,
		},
		{
			input:    []int{3, 1, 2, 4, 5},
			expected: 12,
		},
		{
			input:    []int{2, 1, 8, 6, 4, 6, 5, 5},
			expected: 25,
		},
	}

	for idx, test_case := range test_cases {
		t.Run(fmt.Sprintf("Test_case_no:%d", idx+1), func(t *testing.T) {
			actual := MaxAmountOfWater(test_case.input)
			if actual != test_case.expected {
				t.Errorf("Testing Max amount of water. Input: %v, Expected: %d, Actual: %d", test_case.input, test_case.expected, actual)
			}
		})
	}
}
