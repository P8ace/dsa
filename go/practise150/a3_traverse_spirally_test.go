package practise150

import (
	"fmt"
	"reflect"
	"testing"
)

func TestTraverseSpirally(t *testing.T) {
	test_cases := []struct {
		input    [][]int
		expected []int
	}{
		{
			input:    [][]int{{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}},
			expected: []int{1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10},
		},
	}

	for idx, test_case := range test_cases {
		t.Run(fmt.Sprintf("Test_case_no:%d", idx+1), func(t *testing.T) {
			actual := TraverseSpirally(test_case.input)
			if !reflect.DeepEqual(actual, test_case.expected) {
				t.Errorf("Testing Traversing spirally. Input: %v, Expected: %v, Actual: %v.", test_case.input, test_case.expected, actual)
			}
		})
	}
}
