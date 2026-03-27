package practise150

import (
	"fmt"
	"reflect"
	"testing"
)

func Test_top_k_frequent(t *testing.T) {
	test_cases := []struct {
		input    []int
		k        int
		expected []int
	}{
		{
			input:    []int{1, 2, 2, 3, 3},
			k:        2,
			expected: []int{3, 2},
		},
		{
			input:    []int{7, 7},
			k:        1,
			expected: []int{7},
		},
		{
			input:    []int{3, 1, 4, 4, 5, 2, 6, 1},
			k:        2,
			expected: []int{4, 1},
		},
		{
			input:    []int{7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9},
			k:        4,
			expected: []int{5, 11, 7, 10},
		},
	}

	for i, test_case := range test_cases {
		t.Run(fmt.Sprintf("Test_case_no:%d", i+1), func(t *testing.T) {
			actual := top_k_frequenct_elements(test_case.input, test_case.k)
			if !reflect.DeepEqual(actual, test_case.expected) {
				t.Errorf("Input: %v, k: %v, Expected: %v, Actual: %v", test_case.input, test_case.k, test_case.expected, actual)
			}
		})
	}
}
