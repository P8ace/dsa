package practise150

import (
	"fmt"
	"testing"
)

func TestFruitsIntoBaskets(t *testing.T) {
	test_cases := []struct {
		input    []int
		expected int
	}{
		{
			input:    []int{1, 2, 1},
			expected: 3,
		},
		{
			input:    []int{0, 1, 2, 2},
			expected: 3,
		},
		{
			input:    []int{1, 2, 3, 2, 2},
			expected: 4,
		},
	}
	for idx, tc := range test_cases {
		t.Run(fmt.Sprintf("Test_case_no:%d", idx+1), func(t *testing.T) {
			actual := FruitsIntoBasket(tc.input)
			if actual != tc.expected {
				t.Errorf("Testing fruits into baskets. Input: %v, Expected: %d, Actual: %d.\n", tc.input, tc.expected, actual)
			}
		})
	}
}
