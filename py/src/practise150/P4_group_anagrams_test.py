from src.practise150.p4_group_anagrams import Solution

def test_group_anagrams():
    
    test_cases =[
        (["act","pots","tops","cat","stop","hat"], [['act', 'cat'], ['pots', 'tops', 'stop'], ['hat']]),
        (["x"], [["x"]]),
        ([""],[[""]])
        
    ]
    
    s = Solution()
    for test_case in test_cases:
        result = s.group_anagrams(test_case[0])
        assert result == test_case[1]