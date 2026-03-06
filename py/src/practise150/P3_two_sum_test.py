from src.practise150.p3_two_sum import Solution

def test_two_sum():
    test_cases =[
        ([3,4,5,6],7,[0,1]),
        ([4,5,6],10,[0,2]),
        ([5,5],10,[0,1])
    ]
    s = Solution()
    for test_case in test_cases:
        result = s.two_sum(test_case[0],test_case[1])
        assert  result == test_case[2]
    for test_case in test_cases:
        result = s.two_sum2(test_case[0],test_case[1])
        assert  result == test_case[2]
    