from src.practise150.p2_valid_anagram import Solution

def test_valid_anagram():
    test_cases = [
        ("racecar","carrace",True),
        ("jem","mej", True),
        ("cable","able",False),
        ("jar","jam",False),
        ("listen","silent",True)
    ]
    
    s = Solution()
    
    for test_case in test_cases:
        result = s.isAnagram(test_case[0],test_case[1])
        assert result == test_case[2]
    for test_case in test_cases:
        result = s.isAnagram2(test_case[0],test_case[1])
        assert result == test_case[2]
    for test_case in test_cases:
        result = s.isAnagram3(test_case[0],test_case[1])
        assert result == test_case[2]