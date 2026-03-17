from src.practise150.p17_longest_substring_with_replacement import Solution

def test_longest_substring():
    
    test_cases = [
        ("XYYX", 2, 4),
        ("AAABABB", 1 , 5)
    ]
    s= Solution()
    
    for test_case in test_cases:
        assert test_case[2] == s.longest_substring(test_case[0], test_case[1])