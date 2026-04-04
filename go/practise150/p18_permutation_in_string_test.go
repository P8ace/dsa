package practise150

import (
	"fmt"
	"testing"
)

func TestPermutationInString(t *testing.T) {
	test_cases := []struct {
		input1   string
		input2   string
		expected bool
	}{
		{
			input1:   "abc",
			input2:   "lecabee",
			expected: true,
		},
		{
			input1:   "abc",
			input2:   "lecaabee",
			expected: false,
		},
	}

	for idx, tc := range test_cases {
		t.Run(fmt.Sprintf("Test_case_no:%d", idx+1), func(t *testing.T) {
			actual := CheckPermutation(tc.input1, tc.input2)
			if actual != tc.expected {
				t.Errorf("Testing permutation in string. Input1: %s, Input2: %s, Expected: %v, Actual: %v.", tc.input1, tc.input2, tc.expected, actual)
			}
		})
	}
}
