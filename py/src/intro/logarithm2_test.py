from intro.logarithm2 import log_scale

run_cases = [
    ([1, 10, 100, 1000], 10, [0.0, 1.0, 2.0, 3.0]),
    ([1, 2, 4, 8], 2, [0.0, 1.0, 2.0, 3.0]),
]

submit_cases = run_cases + [
    ([2, 4, 8, 16], 2, [1.0, 2.0, 3.0, 4.0]),
    ([3, 9, 27, 81], 3, [1.0, 2.0, 3.0, 4.0]),
    ([5, 25, 125, 625], 5, [1.0, 2.0, 3.0, 4.0]),
    ([10, 100, 1000, 10000], 10, [1.0, 2.0, 3.0, 4.0]),
    ([20, 400, 8000, 160000], 20, [1.0, 2.0, 3.0, 4.0]),
]


def test_log_scale():
    result = []
    for test_case in submit_cases:
        expected_output = test_case[2]
        result = log_scale(test_case[0], test_case[1])
    for i in range(0, len(result)):
            result[i] = round(result[i], 2)
    assert result == expected_output
