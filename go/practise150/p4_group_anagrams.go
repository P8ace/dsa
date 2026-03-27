package practise150

// """
// Given an array of strings, group all anagrams together into sublists. You may return the output in any order.

// Eg:
//     Input: strs = ["act","pots","tops","cat","stop","hat"]

//     Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

//     Input: strs = ["x"]

//     Output: [["x"]]
// """

func group_anagrams(sliceofstrings []string) [][]string {
	res1 := make(map[[26]int][]string)

	for _, a_string := range sliceofstrings {
		frequency_array := [26]int{}
		for _, rune := range a_string {
			frequency_array[rune-'a']++
		}
		res1[frequency_array] = append(res1[frequency_array], a_string)
	}

	var final [][]string
	for _, val := range res1 {
		final = append(final, val)
	}

	return final
}
