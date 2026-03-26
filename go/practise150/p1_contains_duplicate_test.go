package practise150

import "testing"

func Test_contains_duplicate(t *testing.T) {
	test_cases := []struct {
		input    []int
		expected bool
	}{
		{
			input:    []int{1, 2, 3, 1},
			expected: true,
		},
		{
			input:    []int{1, 4, 3, 5},
			expected: false,
		},
		{
			input:    []int{1, 2, 3, 11, 12, 4, 3, 2},
			expected: true,
		},
	}

	for _, test_case := range test_cases {
		t.Run("", func(t *testing.T) {
			actual := contains_duplicate(test_case.input)
			if actual != test_case.expected {
				t.Errorf("Checking for duplicates. Expected : %t, Actual : %t", test_case.expected, actual)
			}
		})
	}

}
