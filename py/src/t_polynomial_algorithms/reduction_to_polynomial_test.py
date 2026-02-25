from src.t_polynomial_algorithms.reduction_to_polynomial import fib

run_cases = [
    (1, 1),
    (4, 3),
    (10, 55),
    (20, 6765),
]

submit_cases = run_cases + [
    (0, 0),
    (40, 102334155),
    (70, 190392490709135),
    (160, 1226132595394188293000174702095995),
]


def test_fib():
    for test_case in submit_cases:
        expected_output = test_case[1]
        result = fib(test_case[0])
        assert result == expected_output
