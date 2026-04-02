package practise150

import (
	"fmt"
	"testing"
)

func TestTrapRain(t *testing.T) {
	type TestCase struct {
		input    []int
		expected int
	}
	test_cases := []TestCase{
		{
			input:    []int{0, 2, 0, 3, 1, 0, 1, 3, 2, 1},
			expected: 9,
		},
		{
			input:    []int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1},
			expected: 6,
		},
		{
			input:    []int{4, 2, 0, 3, 2, 5},
			expected: 9,
		},
	}

	for idx, test_case := range test_cases {
		t.Run(fmt.Sprintf("Test_case_No:%d", idx+1), func(t *testing.T) {
			actual := TrapRain(test_case.input)
			if actual != test_case.expected {
				t.Errorf("Testing Trap Rain. Input: %v, Expected: %d, Actual: %d", test_case.input, test_case.expected, actual)
			}
		})
	}
}
