package practise150

import (
	"fmt"
	"testing"
)

func TestLongestSubstringWithReplacement(t *testing.T) {
	test_cases := []struct {
		input    string
		k        int
		expected int
	}{
		{"XYYX", 2, 4},
		{"AAABABB", 1, 5},
	}

	for idx, test_case := range test_cases {
		t.Run(fmt.Sprintf("test_case_no:%d", idx+1), func(t *testing.T) {
			actual := LongestSubstringWithReplacement(test_case.input, test_case.k)
			if actual != test_case.expected {
				t.Errorf("Testing Longest substring with k replacements. Input: %s, K: %d, Expected: %d, Actual: %d.\n",
					test_case.input,
					test_case.k,
					test_case.expected,
					actual)
			}
		})
	}
}
