package practise150

// You are given a string s consisting of only uppercase english characters and an integer k.
// You can choose up to k characters of the string and replace them with any other uppercase English character.
// After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

func LongestSubstringWithReplacement(s string, k int) int {
	i, length := 0, 0
	hashset := make(map[rune]int)
	temp := 0

	for j, rn := range s {
		hashset[rn]++
		temp = max(temp, hashset[rn])

		for j-i+1-temp > k {
			hashset[rune(s[i])]--
			i++
		}

		length = max(length, j-i+1)

	}

	return length
}
