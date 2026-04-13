package practise150

import (
	"fmt"
	"testing"
)

func TestDifferenceStringInt(t *testing.T) {
	test_cases := []struct {
		s1       string
		s2       string
		expected int
	}{
		{
			s1:       "100",
			s2:       "98",
			expected: 2,
		},
		{
			s1:       "10",
			s2:       "100",
			expected: -90,
		},
	}
	for idx, tc := range test_cases {
		t.Run(fmt.Sprintf("Test_case_no:%d", idx+1), func(t *testing.T) {
			actual := DifferenceOfStringInts(tc.s1, tc.s2)
			if actual != tc.expected {
				t.Errorf("Testing difference string ints. S1: %s, S2: %s, Expected: %d, Actual: %d\n", tc.s1, tc.s2, tc.expected, actual)
			}
		})
	}
}
