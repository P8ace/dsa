package algo

import "math"

/************************************************************************************************** */
func IsEven(n int) bool {
	if n%2 == 0 {
		return true
	}
	return false
}

/*
  - Using Bitwise and operator with binary 1, will result in either 1 or 0.
  - If the result is 0, then it is a even number else odd.
  - Example: 5 & 1
  - 1 1 1 1
    &  	0 0 0 1
    -----------
    0 0 0 1 , so this we can say it is an odd number.
*/
func IsEvenBitwise(n int) bool {
	if n&1 == 0 {
		return true
	}
	return false
}

/************************************************************************************************** */

// Sum of first n natural numbers
// Given a positive integer n, we have to find the sum of first n natural numbers.
func SumofNaturals(n int) int {
	// time O(n)
	// space O(1)
	sum := 0

	for i := 1; i <= n; i++ {
		sum += i
	}
	return sum
}

func SumofNaturalsRecursion(n int) int {
	// time O(n)
	// space O(n)
	if n == 1 {
		return 1
	}
	return n + SumofNaturalsRecursion(n-1)
}

func SumofNaturalsFormula(n int) int {
	// time O(1)
	// space O(1)
	return (n * (n + 1)) / 2
}

/************************************************************************************************** */

// sum of squares
// Given a positive integer n, we have to find the sum of squares of first n natural numbers.
func SumofSquares(n int) int {
	//time O(n)
	// space O(1)
	sum := 0

	for i := 1; i <= n; i++ {
		sum += i * i
	}
	return sum
}

func SumofSquaresFormula(n int64) int64 {
	// n(n+1)(2n+1)/6
	// time O(1)
	// space O(1)
	return (n * (n + 1) * (2*n + 1)) / 6
}

/************************************************************************************************** */
// Given two integers n and m (m!=0), find the number closest to n and is divisible by m.
// If there is more than one, then return the one with the maximum absolute value.
// Eg: n = 13, m = 4
// Output: 12
// explanation: 12 is closest to 13 and is divisible by 4.
// Eg: n = -15, m = 6
// Output: -18
// explanation: both -12 and -18 are closest to -15, but -18 is has greater absolute value.

func ClosestNumber(n, m int) int {
	// time O(m)
	// space O(1)
	start := n - int(math.Abs(float64(m)))
	end := n + int(math.Abs(float64(m)))

	result := 0
	min_difference := math.MaxInt

	for i := start; i <= end; i++ {
		if i%m == 0 {
			diff := int(math.Abs(float64(n - i)))
			if diff < min_difference || diff == min_difference && math.Abs(float64(i)) > math.Abs(float64(result)) {
				result = i
				min_difference = diff
			}
		}
	}
	return result
}

/************************************************************************************************** */
func SumOfDigits(n int) int {
	sum := 0

	for n > 0 {
		sum += n % 10
		n = n / 10
	}
	return sum
}

/************************************************************************************************** */
func ReverseNumber(n int) int {
	reverse := 0

	for n > 0 {
		reverse = reverse*10 + (n % 10)
		n = n / 10
	}
	return reverse
}

/************************************************************************************************** */
func IsPrimeNumber(n int) bool {
	if n < 2 {
		return false
	}

	for i := 2; i < n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func IsPrimeWithSquareroot(n int) bool {
	if n < 2 {
		return false
	}

	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

/************************************************************************************************** */
func IsPower(x, y int) bool {
	// time: O(logy)
	// space: O(1)

	if x == 1 {
		return y == 1
	}

	product := 1

	for product < y {
		product *= x
		if product == y {
			return true
		}
	}
	return false
}

func IsPowerInLog(x, y int) bool {
	// time: O(1)
	// space: O(1)
	res := math.Log(float64(y)) / math.Log(float64(x))
	return res == math.Floor(res)
}
