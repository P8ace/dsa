from src.practise150.p7_product_of_array_except_self import Solution

def test_product_of_array_except_self():
    test_cases = [
        (
            [1,2,3,4],
            [24,12,8,6]
        ),
        (
            [1,2,4,6],
            [48,24,12,8]
        ),
        (
            [-1,0,1,2,3],
            [0,-6,0,0,0]
        )
    ]
    s = Solution()
    for test_case in test_cases:
        result = s.product_except_self(test_case[0])
        assert result == test_case[1]
    