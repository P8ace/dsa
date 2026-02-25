from src.intro.minimum import find_minimum

run_cases = [
    ([7, 4, 3, 100, 2343243, 343434, 1, 2, 32], 1),
    ([12, 12, 12], 12),
    ([10, 200, 3000, 5000, 4], 4),
]

submit_cases = run_cases + [
    ([1], 1),
    ([1, 2, 3, 4, 5], 1),
    ([5, 4, 3, 2, 1], 1),
    ([100, 200, 300, 400, 500], 100),
    ([500, 400, 300, 200, 100], 100),
    ([], None),
]


def test_find_minimum():
    for test_case in submit_cases:
        expected_output = test_case[1]
        result = find_minimum(test_case[0])
        assert result == expected_output
