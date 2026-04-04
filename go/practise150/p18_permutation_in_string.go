package practise150

import "maps"

// You are given two strings s1 and s2.
// Return true if s2 contains a permutation of s1, or false otherwise.
// That means if a permutation of s1 exists as a substring of s2, then return true.
// Both strings only contain lowercase letters.
// Eg:
//     Input: s1 = "abc", s2 = "lecabee"
//     Output: true

func CheckPermutation(s1, s2 string) bool {
	left, right := 0, len(s1)-1

	s1map := make(map[rune]int)
	tempMap := make(map[rune]int)
	for _, rn := range s1 {
		s1map[rn]++
	}

	for right < len(s2) {
		k := left
		clear(tempMap)
		for k <= right {
			tempMap[rune(s2[k])]++
			k++
		}
		if maps.Equal(tempMap, s1map) {
			return true
		}
		left++
		right++
	}
	return false
}
