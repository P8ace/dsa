from src.t_polynomial_algorithms.exponential_growth import exponential_growth

run_cases = [
    (10, 2, 4, [10, 20, 40, 80, 160]),
    (0, 2, 2, [0, 0, 0]),
    (20, 2, 6, [20, 40, 80, 160, 320, 640, 1280]),
]

submit_cases = run_cases + [
    (30, 3, 3, [30, 90, 270, 810]),
    (
        40,
        10,
        10,
        [
            40,
            400,
            4000,
            40000,
            400000,
            4000000,
            40000000,
            400000000,
            4000000000,
            40000000000,
            400000000000,
        ],
    ),
    (10, 5, 0, [10]),
    (1, 1, 5, [1, 1, 1, 1, 1, 1]),
]


def test_exponential_growth():
    for test_case in submit_cases:
        expected_result = test_case[3]
        result = exponential_growth(test_case[0], test_case[1], test_case[2])
        assert result == expected_result
