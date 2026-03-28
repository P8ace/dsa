package practise150

import (
	"fmt"
	"reflect"
	"testing"
)

func Test_product_of_array_except_self(t *testing.T) {
	test_cases := []struct {
		input    []int
		expected []int
	}{
		{
			input:    []int{1, 2, 3, 4},
			expected: []int{24, 12, 8, 6},
		},
		{
			input:    []int{-1, 2, 3, 1},
			expected: []int{6, -3, -2, -6},
		},
		{
			input:    []int{4, 5, 0, 1},
			expected: []int{0, 0, 20, 0},
		},
	}

	for i, test_case := range test_cases {
		t.Run(fmt.Sprintf("Test_Case_No:%d", i+1), func(t *testing.T) {
			actual := product_of_array_except_self(test_case.input)
			if !reflect.DeepEqual(actual, test_case.expected) {
				t.Errorf("Testing product except self, Input: %v, Expected: %v, Actual: %v", test_case.input, test_case.expected, actual)
			}
		})
	}
}
