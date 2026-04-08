package practise150

import (
	"fmt"
	"reflect"
	"testing"
)

func TestMoveZeroes(t *testing.T) {
	test_cases := []struct {
		input    []int
		expected []int
	}{
		{
			input:    []int{0, 0, 1, 2, 0, 5},
			expected: []int{1, 2, 5, 0, 0, 0},
		},
		{
			input:    []int{0, 1, 0},
			expected: []int{1, 0, 0},
		},
		{
			input:    []int{1, 2, 0, 3, 0, 5, 0},
			expected: []int{1, 2, 3, 5, 0, 0, 0},
		},
		{
			input:    []int{10, 20, 30},
			expected: []int{10, 20, 30},
		},
	}

	for idx, test_case := range test_cases {
		t.Run(fmt.Sprintf("Test_case_no:%d", idx+1), func(t *testing.T) {
			original := make([]int, len(test_case.input))
			copy(original, test_case.input)
			MoveZeroes(test_case.input)
			if !reflect.DeepEqual(test_case.input, test_case.expected) {
				t.Errorf("testing move zeroes. Input: %v, Expected: %v, Actual: %v.", original, test_case.expected, test_case.input)
			}
		})
	}
}
