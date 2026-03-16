from src.practise150.p11_two_sum_indexed1 import Solution

def test_two_sum_indexed1():
    test_cases= [
        ([1,2,3,4],3,[1,2]),
        ([7,11,13,19], 24, [2,3])
    ]
    s = Solution()
    for test_case in test_cases:
        result = s.two_sum(test_case[0], test_case[1])
        assert result == test_case[2]
    for test_case in test_cases:
        result = s.two_sum2(test_case[0], test_case[1])
        assert result == test_case[2]