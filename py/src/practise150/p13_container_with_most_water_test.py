from src.practise150.p13_container_with_most_water import Solution

def test_max_area():
    test_cases = [
        ([1,7,2,5,4,7,3,6], 36),
        ([2,2,2],4),
        ([1,5,4,3], 6),
        ([3,1,2,4,5],12),
        ([2,1,8,6,4,6,5,5],25),
    ]
    s = Solution()
    for test_case in test_cases:
        result = s.maxArea(test_case[0])
        assert result == test_case[1]