package practise150

import (
	"fmt"
	"testing"
)

func Test_valid_anagram(t *testing.T) {
	test_cases := []struct {
		input1   string
		input2   string
		expected bool
	}{
		{
			input1:   "racecar",
			input2:   "carrace",
			expected: true,
		},
		{
			input1:   "jem",
			input2:   "mej",
			expected: true,
		},
		{
			input1:   "cable",
			input2:   "able",
			expected: false,
		},
		{
			input1:   "jar",
			input2:   "jam",
			expected: false,
		},
		{
			input1:   "listen",
			input2:   "silent",
			expected: true,
		},
	}

	for i, test_case := range test_cases {
		t.Run(fmt.Sprintf("Testing valid anagram: TestCase no: %d", i+1), func(t *testing.T) {
			actual := valid_anagram(test_case.input1, test_case.input2)
			if actual != test_case.expected {
				t.Errorf("Testing valid anagram for s : %s, t : %s, expected : %t, actual: %t", test_case.input1, test_case.input2, test_case.expected, actual)
			}
		})
	}
	for i, test_case := range test_cases {
		t.Run(fmt.Sprintf("Testing valid anagram 2: TestCase no: %d", i+1), func(t *testing.T) {
			actual := valid_anagram2(test_case.input1, test_case.input2)
			if actual != test_case.expected {
				t.Errorf("Testing valid anagram for s : %s, t : %s, expected : %t, actual: %t", test_case.input1, test_case.input2, test_case.expected, actual)
			}
		})
	}
}
