package practise150

import (
	"fmt"
	"testing"
)

func TestPivotIndex(t *testing.T) {
	test_cases := []struct {
		input    []int
		expected int
	}{
		{
			input:    []int{1, 7, 3, 6, 5, 6},
			expected: 3,
		},
		{
			input:    []int{3, 2, 1},
			expected: -1,
		},
		{
			input:    []int{2, 1, -1},
			expected: 0,
		},
	}
	for idx, tc := range test_cases {
		t.Run(fmt.Sprintf("Test_case_No:%d", idx+1), func(t *testing.T) {
			actual := PivotIndex(tc.input)
			if actual != tc.expected {
				t.Errorf("Testing pivot index. Input: %v, Expected: %d, Actual: %d\n", tc.input, tc.expected, actual)
			}
		})
	}
}
