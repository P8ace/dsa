from src.practise150.p16_longest_substring_without_duplicates import Solution


def test_longest_substring():
    test_cases = [
        ("abcabcbb", 3),
        ("bbbb",1),
        ("bbbbb", 1),
        ("pwwkew",3),
        ("wkew",3)
    ]
    
    s = Solution()
    
    for test_case in test_cases:
        assert test_case[1] == s.longestsubstring(test_case[0])