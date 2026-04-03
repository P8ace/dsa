package practise150

import (
	"fmt"
	"testing"
)

type testCase struct {
	input    []int
	expected int
}

func TestMaxProfit(t *testing.T) {
	test_cases := []testCase{
		{
			input:    []int{10, 1, 5, 6, 7, 1},
			expected: 6,
		},
		{
			input:    []int{10, 8, 7, 5, 2},
			expected: 0,
		},
	}

	for idx, test_case := range test_cases {
		t.Run(fmt.Sprintf("Test_case_no:%d", idx+1), func(t *testing.T) {
			actual := MaxProfit(test_case.input)
			if actual != test_case.expected {
				t.Errorf("Testing best stock to sell. Input; %v, Expected: %d, Actual: %d", test_case.input, test_case.expected, actual)
			}
		})
	}
}
