package practise150

func DifferenceOfStringInts(s1, s2 string) int {
	i1 := 0
	for _, rn := range s1 {
		i1 = (i1 * 10) + int(rn-'0')
	}

	i2 := 0
	for _, rn2 := range s2 {
		i2 = (i2 * 10) + int(rn2-'0')
	}

	return i1 - i2
}
