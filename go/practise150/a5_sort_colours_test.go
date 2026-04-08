package practise150

import (
	"fmt"
	"reflect"
	"testing"
)

func TestSortColours(t *testing.T) {
	test_cases := []struct {
		input    []int
		expected []int
	}{
		{
			input:    []int{1, 0, 1, 2},
			expected: []int{0, 1, 1, 2},
		},
		{
			input:    []int{2, 1, 0},
			expected: []int{0, 1, 2},
		},
	}
	for idx, test_case := range test_cases {
		t.Run(fmt.Sprintf("test_case_no:%d", idx+1), func(t *testing.T) {
			original := make([]int, len(test_case.input))
			copy(original, test_case.input)
			sortColours(test_case.input)
			if !reflect.DeepEqual(test_case.input, test_case.expected) {
				t.Errorf("Testing sort colours. Input: %v, Expected: %v, Actual: %v.", original, test_case.expected, test_case.input)
			}
		})
	}
}
