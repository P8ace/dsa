from src.practise150.p12_three_sum import Solution

def test_three_sum():
    test_cases = [
        ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
        ([0,1,1], []),
        ([0,0,0], [[0,0,0]])
    ]
    
    s = Solution()
    for test_case in test_cases:
        result = s.three_sum(test_case[0])
        assert result == test_case[1]