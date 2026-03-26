package practise150

//Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

// Eg;
//     Input: s = "racecar", t = "carrace"

//     Output: true

func valid_anagram(s, t string) bool {
	if len(s) != len(t) {
		return false
	}

	smap := make(map[rune]int)
	tmap := make(map[rune]int)

	for i, item := range s {
		smap[item]++
		tmap[rune(t[i])]++
	}

	for key, value := range smap {
		if v2, ok := tmap[key]; !ok || v2 != value {
			return false
		}
	}
	return true
}

func valid_anagram2(s, t string) bool {
	if len(s) != len(t) {
		return false
	}

	frequency_array := [26]int{}

	for i := 0; i < len(s); i++ {
		frequency_array[s[i]-'a']++
		frequency_array[t[i]-'a']--
	}

	for _, value := range frequency_array {
		if value != 0 {
			return false
		}
	}
	return true
}
