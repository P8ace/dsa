package algo

import (
	"fmt"
	"testing"
)

func TestIsEven(t *testing.T) {
	test_cases := []struct {
		input    int
		expected bool
	}{
		{2, true},
		{3, false},
		{11, false},
		{16, true},
	}

	for idx, tc := range test_cases {
		t.Run(fmt.Sprintf("Test_case_no:%d", idx+1), func(t *testing.T) {
			actual := IsEven(tc.input)
			if actual != tc.expected {
				t.Errorf("Testing is Even. Input: %d, Expected: %t, Actual: %t.\n", tc.input, tc.expected, actual)
			}
		})
	}
}

func TestIsEvenBitwise(t *testing.T) {
	test_cases := []struct {
		input    int
		expected bool
	}{
		{2, true},
		{3, false},
		{11, false},
		{16, true},
	}

	for idx, tc := range test_cases {
		t.Run(fmt.Sprintf("Test_case_no:%d", idx+1), func(t *testing.T) {
			actual := IsEvenBitwise(tc.input)
			if actual != tc.expected {
				t.Errorf("Testing is Even. Input: %d, Expected: %t, Actual: %t.\n", tc.input, tc.expected, actual)
			}
		})
	}
}

func TestSumofNaturalNumbers(t *testing.T) {
	t.Run("Testing Naive approach", func(t *testing.T) {
		actual := SumofNaturals(10)
		if actual != 55 {
			t.Errorf("Testing sum of Naturals. Input: %d, Expected: %d, actual: %d", 10, 55, actual)
		}
	})
	t.Run("Testing Recursion approach", func(t *testing.T) {
		actual := SumofNaturalsRecursion(10)
		if actual != 55 {
			t.Errorf("Testing sum of Naturals Recursion. Input: %d, Expected: %d, actual: %d", 10, 55, actual)
		}
	})
	t.Run("Testing Formula approach", func(t *testing.T) {
		actual := SumofNaturalsFormula(10)
		if actual != 55 {
			t.Errorf("Testing sum of Naturals with Formula. Input: %d, Expected: %d, actual: %d", 10, 55, actual)
		}
	})
}

func TestSumofSquaresofNaturalNumbers(t *testing.T) {
	t.Run("Testing Naive approach", func(t *testing.T) {
		actual := SumofSquares(10)
		if actual != 385 {
			t.Errorf("Testing sum of Naturals. Input: %d, Expected: %d, actual: %d", 10, 385, actual)
		}
	})
	t.Run("Testing Formula approach", func(t *testing.T) {
		actual := SumofSquaresFormula(10)
		if actual != 385 {
			t.Errorf("Testing sum of Naturals with Formula. Input: %d, Expected: %d, actual: %d", 10, 385, actual)
		}
	})
}

/************************************************************************************************** */
func TestClosestNumber(t *testing.T) {
	t.Run("Testing Naive approach", func(t *testing.T) {
		actual := ClosestNumber(13, 4)
		if actual != 12 {
			t.Errorf("Testing closest number to n, divisible by m. Input: %d, M: %d, Expected: %d, actual: %d", 13, 4, 12, actual)
		}
	})
}

/************************************************************************************************** */
func TestSumofDigits(t *testing.T) {
	if SumOfDigits(1234) != 10 {
		t.Error("Error while summing the digits of n")
	}
}

/************************************************************************************************** */
func TestReverseNumber(t *testing.T) {
	test_cases := []struct {
		input    int
		expected int
	}{
		{123, 321},
		{400, 4},
		{4562, 2654},
	}
	for _, tc := range test_cases {
		t.Run("testing reverse number", func(t *testing.T) {
			actual := ReverseNumber(tc.input)

			if actual != tc.expected {
				t.Errorf("error while testing reverese number. Input: %d, Expected: %d, Actual: %d.\n", tc.input, tc.expected, actual)
			}
		})
	}
}

/************************************************************************************************** */
func TestIsPrimeNumber(t *testing.T) {
	test_cases := []struct {
		input    int
		expected bool
	}{
		{123, false},
		{400, false},
		{17, true},
		{13, true},
	}
	for _, tc := range test_cases {
		t.Run("testing is prime number", func(t *testing.T) {
			actual := IsPrimeNumber(tc.input)

			if actual != tc.expected {
				t.Errorf("error while testing prime number. Input: %d, Expected: %t, Actual: %t.\n", tc.input, tc.expected, actual)
			}
		})
	}
	for _, tc := range test_cases {
		t.Run("testing is prime number with square root method", func(t *testing.T) {
			actual := IsPrimeNumber(tc.input)

			if actual != tc.expected {
				t.Errorf("error while testing prime number. Input: %d, Expected: %t, Actual: %t.\n", tc.input, tc.expected, actual)
			}
		})
	}
}

/************************************************************************************************** */
func TestIsPower(t *testing.T) {
	test_cases := []struct {
		input    int
		input2   int
		expected bool
	}{
		{2, 128, true},
		{2, 30, false},
		{7, 49, true},
	}
	for _, tc := range test_cases {
		t.Run("testing is power", func(t *testing.T) {
			actual := IsPower(tc.input, tc.input2)

			if actual != tc.expected {
				t.Errorf("error while testing power of. Input: %d, Input2: %d, Expected: %t, Actual: %t.\n", tc.input, tc.input2, tc.expected, actual)
			}
		})
	}
	for _, tc := range test_cases {
		t.Run("testing is power of with log method", func(t *testing.T) {
			actual := IsPowerInLog(tc.input, tc.input2)

			if actual != tc.expected {
				t.Errorf("error while testing is power of with log method. Input: %d, Input2: %d, Expected: %t, Actual: %t.\n", tc.input, tc.input2, tc.expected, actual)
			}
		})
	}
}
