package practise150

import "unicode"

//Given a string s, return true if it is a palindrome, otherwise return false.
// A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
// Eg:
//     Input: s = "Was it a car or a cat I saw?"
//     Output: true

func isPalindrome(s string) bool {
	i := 0
	j := len(s) - 1 
	
	for i < j{
		for i < j && !isAlphaNumeric(rune(s[i])) {
			i++
		}
		for i < j && !isAlphaNumeric(rune(s[j])) {
			j--
		}
		if unicode.ToLower(rune(s[i])) != unicode.ToLower(rune(s[j])) {
			return false
		}
		i++
		j--
	}
	return true
}

func isAlphaNumeric(r rune) bool{
	return unicode.IsLetter(r) || unicode.IsNumber(r)
}