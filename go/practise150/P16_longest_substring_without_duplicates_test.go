package practise150

import (
	"fmt"
	"testing"
)

func TestLongestSubstring(t *testing.T) {
	test_cases := []struct {
		input    string
		expected int
	}{
		{
			input:    "abcabcbb",
			expected: 3,
		},
		{
			input:    "bbbb",
			expected: 1,
		},
		{
			input:    "bbbbb",
			expected: 1,
		},
		{
			input:    "pwwkew",
			expected: 3,
		},
		{
			input:    "wkew",
			expected: 3,
		},
		{
			input:    "bbcc",
			expected: 2,
		},
	}

	for idx, test_case := range test_cases {
		t.Run(fmt.Sprintf("Test_Case_no:%d", idx+1), func(t *testing.T) {
			actual := LongestSubstring(test_case.input)
			if actual != test_case.expected {
				t.Errorf("Testing Longest Substring. Input: %s, Expected: %d. Actual: %d.", test_case.input, test_case.expected, actual)
			}
		})
		t.Run(fmt.Sprintf("Test_Case_no:%d", idx+1), func(t *testing.T) {
			actual := LongestSubstringWithTwoPointers(test_case.input)
			if actual != test_case.expected {
				t.Errorf("Testing Longest Substring. Input: %s, Expected: %d. Actual: %d.", test_case.input, test_case.expected, actual)
			}
		})
	}
}
