package practise150

import (
	"fmt"
	"testing"
)

func TestValidPalindrome(t *testing.T) {
	test_cases := []struct {
		input    string
		expected bool
	}{
		{
			input:    "Was it a car or a cat I saw?",
			expected: true,
		},
		{
			input:    "tab a cat",
			expected: false,
		},
	}

	for idx, test_case := range test_cases {
		t.Run(fmt.Sprintf("Test_case_no:%d", idx+1), func(t *testing.T) {
			actual := isPalindrome(test_case.input)
			if actual != test_case.expected {
				t.Errorf("Testing isPalindrome function. Input: %s, Expected: %v, Actual: %v", test_case.input, test_case.expected, actual)
			}
		})
	}

}
