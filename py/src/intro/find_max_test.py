from src.intro.find_max import max

run_cases = [([7, 4, 3, 100, 2343243, 343434, 1, 2, 32], 2343243), ([12, 12, 12], 12)]

submit_cases = run_cases + [
    ([10, 200, 3000, 5000, 4], 5000),
    ([0], 0),
    ([-1, -2, -3], -1),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 10),
]


def test_find_max():
    for test_case in submit_cases:
        expected_output = test_case[1]
        result = max(test_case[0])
        assert result == expected_output
