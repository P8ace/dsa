from src.intro.factorial import factorial

run_cases = [(2, 2), (3, 6), (5, 120)]

submit_cases = run_cases + [
    (1, 1),
    (6, 720),
    (7, 5040),
    (8, 40320),
    (9, 362880),
    (11, 39916800),
]


def test_factorial():
    for test_case in submit_cases:
        expected_output = test_case[1]
        result = factorial(test_case[0])
        assert result == expected_output
