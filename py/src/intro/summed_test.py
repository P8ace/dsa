from intro.summed import summed

run_cases = [([7, 4, 3, 100, 2343243, 343434, 1, 2, 32], 2686826), ([12, 12, 12], 36)]

submit_cases = run_cases + [
    ([10, 200, 3000, 5000, 4], 8214),
    ([], 0),
    ([1], 1),
    ([123456789], 123456789),
    ([-1, -2, -3], -6),
    ([0, 0, 0, 0, 0], 0),
]


def test_summed():
    for test_case in submit_cases:
        expected_output = test_case[1]
        result = summed(test_case[0])
        assert result == expected_output
