package practise150

import (
	"fmt"
	"reflect"
	"testing"
)

func Test_group_anagrams(t *testing.T) {
	test_cases := []struct {
		input    []string
		expected [][]string
	}{
		{
			input:    []string{"act", "pots", "tops", "cat", "stop", "hat"},
			expected: [][]string{{"act", "cat"}, {"pots", "tops", "stop"}, {"hat"}},
		},
		{
			input:    []string{"x"},
			expected: [][]string{{"x"}},
		},
		{
			input:    []string{""},
			expected: [][]string{{""}},
		},
	}

	for i, test_case := range test_cases {
		t.Run(fmt.Sprintf("Test_case_no:%d", i+1), func(t *testing.T) {
			actual := group_anagrams(test_case.input)
			if !reflect.DeepEqual(actual, test_case.expected) {
				t.Errorf("Input: %v, Expected: %v, Actual: %v", test_case.input, test_case.expected, actual)
			}
		})
	}
}
