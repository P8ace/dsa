from src.practise150.p18_permuation_in_string import Solution

def test_permutation_in_string():
    test_cases=[
        ("abc", "lecabee", True),
        ("abc", "lecaabee", False)
    ]
    s = Solution()
    for test_case in test_cases:
        assert test_case[2] == s.check_permutation(test_case[0], test_case[1])