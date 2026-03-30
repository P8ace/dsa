package sorting

import (
	"fmt"
	"reflect"
	"testing"
)

func TestMergeSort(t *testing.T) {
	test_cases := []struct {
		input    []int
		expected []int
	}{
		{
			input:    []int{3, 2, 1},
			expected: []int{1, 2, 3},
		},
		{
			input:    []int{5, 4, 3, 2, 1},
			expected: []int{1, 2, 3, 4, 5},
		},
		{
			input:    []int{4, -7, 1, 0, 5},
			expected: []int{-7, 0, 1, 4, 5},
		},
		{
			input:    []int{11, 22, 33, 12, 0},
			expected: []int{0, 11, 12, 22, 33},
		},
	}

	for idx, test_case := range test_cases {
		t.Run(fmt.Sprintf("Test_case_no:%d", idx + 1), func(t *testing.T) {
			actual := mergeSort(test_case.input)
			if reflect.DeepEqual(actual, test_case.expected) {
				t.Errorf("Failed Test for merge sort. Input: %v, Expected: %v, Actual: %v", test_case.input, test_case.expected, actual)
			}
		})
	}
}
