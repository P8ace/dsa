package practise150

import (
	"fmt"
	"reflect"
	"testing"
)

func TestTwoSumIndexed1(t *testing.T) {
	test_cases := []struct {
		input    []int
		target   int
		expected []int
	}{
		{
			input:    []int{1, 2, 3, 4},
			target:   3,
			expected: []int{1, 2},
		},
		{
			input:    []int{7, 11, 13, 19},
			target:   24,
			expected: []int{2, 3},
		},
		{
			input:    []int{-1, 1, 5, 5, 7},
			target:   6,
			expected: []int{2, 3},
		},
	}

	for idx, test_case := range test_cases {
		t.Run(fmt.Sprintf("Test_case_no:%d", idx+1), func(t *testing.T) {
			actual := TwoSumIndexed1(test_case.input, test_case.target)
			if !reflect.DeepEqual(actual, test_case.expected) {
				t.Errorf("Testing Two sum indexed 1. Input: %v, Target: %d, Expected: %v, Actual %v.", test_case.input, test_case.target, test_case.expected, actual)
			}
		})
	}

	for idx, test_case := range test_cases {
		t.Run(fmt.Sprintf("Test_case_no:%d", idx+1), func(t *testing.T) {
			actual := TwoSumIndexed1(test_case.input, test_case.target)
			if !reflect.DeepEqual(actual, test_case.expected) {
				t.Errorf("Testing Two sum indexed 1 with Two Pointers. Input: %v, Target: %d, Expected: %v, Actual %v.",
					test_case.input, test_case.target, test_case.expected, actual)
			}
		})
	}
}
