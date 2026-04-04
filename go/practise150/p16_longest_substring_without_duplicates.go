package practise150

// Given a string s, find the length of the longest substring without duplicate characters.

func LongestSubstring(s string) int {
	// Dont use this. Use the one with two pointers.
	hashmap := make(map[rune]struct{})
	
	maxlength := 0
	length := 0
	for _, rn := range s {
		if _, ok := hashmap[rn]; !ok {
			hashmap[rn] = struct{}{}
			length += 1
		} else {
			clear(hashmap)
			hashmap[rn] = struct{}{}
			length = 1
		}
		maxlength = max(length, maxlength)
	}
	return maxlength
}

func LongestSubstringWithTwoPointers(s string) int{
	i, j, length := 0, 0, 0
	
	hashset:= make(map[rune]struct{})
	
	for j < len(s) {
		if _, ok := hashset[rune(s[j])]; !ok {
			hashset[rune(s[j])] = struct{}{}
			length = max(length, j - i + 1)
			j += 1
		} else {
			delete(hashset, rune(s[i]))
			i += 1
		}
	}
	return length
}