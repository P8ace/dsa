package practise150

// Given a string s, find the length of the longest substring without duplicate characters.

func LongestSubstring(s string) int {
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