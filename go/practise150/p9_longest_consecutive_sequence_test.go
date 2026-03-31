package practise150

import (
	"fmt"
	"reflect"
	"testing"
)

func Test_longest_consecutive_sequence(t *testing.T) {
	test_cases := []struct {
		input    []int
		expected int
	}{
		{
			input:    []int{2,20,4,10,3,5,5},
			expected: 4,
		},
		{
			input:    []int{0,3,2,4,5,6,1,1},
			expected: 7,
		},
		{
			input:    []int{-2, 3, -1, 0, 4, -3},
			expected: 4,
		},
	}

	for i, test_case := range test_cases {
		t.Run(fmt.Sprintf("Test_Case_No:%d", i+1), func(t *testing.T) {
			actual := LongestConsecutiveSequence(test_case.input)
			if !reflect.DeepEqual(actual, test_case.expected) {
				t.Errorf("Testing longest consecutive sequence, Input: %v, Expected: %v, Actual: %v", test_case.input, test_case.expected, actual)
			}
		})
	}
}
