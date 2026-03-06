from src.practise150.p1_contains_duplicate import Solution


def test_contains_duplicate():
    test_cases = [([1, 2, 3, 1], True), ([1, 4, 3, 5], False)]
    s = Solution()
    for test_case in test_cases:
        result = s.contains_duplicate(test_case[0])

        assert result == test_case[1]

    for test_case in test_cases:
        result = s.contains_duplicate_2(test_case[0])

        assert result == test_case[1]
