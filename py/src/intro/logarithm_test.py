from intro.logarithm import log

run_cases = [(40000, 0.3, 5), (43000, 0.1, 2), (100000, 0.6, 10)]

submit_cases = run_cases + [
    (1, 1, 0),
    (200, 0.8, 6),
    (300000, 0.5, 9),
    (500000, 0.2, 4),
    (750000, 0.7, 14),
]


def test_log():
    for test_case in submit_cases:
        expected_output = test_case[2]
        result = round(log(test_case[0], test_case[1]))
        assert result == expected_output
