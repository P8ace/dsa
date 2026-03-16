from src.practise150.p14_trap_rain import Solution

def test_trap_rain():
    test_cases = [
        ([0,2,0,3,1,0,1,3,2,1] , 9),
        ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
        ([4,2,0,3,2,5], 9)
    ]
    
    s = Solution()
    for test_case in test_cases:
        result = s.trap(test_case[0])
        assert result == test_case[1]