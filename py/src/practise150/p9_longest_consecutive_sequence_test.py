from src.practise150.p9_longest_consecutive_sequence import Solution

def test_longest_consecutive_sequence():
    test_cases = [
        ([2,20,4,10,3,5,5], 4),
        ([0,3,2,4,5,6,1,1],7)
    ]
    s = Solution()
    for test_case in test_cases:
        result = s.longest_consecutive_sequence(test_case[0])
        assert result == test_case[1]   