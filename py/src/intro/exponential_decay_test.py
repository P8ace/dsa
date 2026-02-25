from src.intro.exponential_decay import exponential_decay

run_cases = [
    (200, 0.5, 1, 100),
    (200, 0.4, 2, 72),
    (200, 0.05, 3, 171),
]

submit_cases = run_cases + [
    (1000, 0.005, 2, 990),
    (1000, 0.05, 3, 857),
    (1200, 0.55, 8, 2),
    (1200, 0.09, 16, 265),
    (0, 0.5, 1, 0),
    (100, 0, 5, 100),
]


def test_exponential_decay():
    for test_case in submit_cases:
        expected_output = test_case[3]
        result = round(exponential_decay(test_case[0], test_case[1], test_case[2]))
        assert result == expected_output
