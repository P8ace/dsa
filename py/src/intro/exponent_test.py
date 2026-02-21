from intro.exponent import exponent

run_cases = [
    ([7, 4, 3, 100, 765, 2344, 1, 2, 32], 5056),
    ([12, 12, 12], 45),
    ([10, 200, 3000, 5000, 4], 11333),
]

submit_cases = run_cases + [
    ([], 0),
    ([1, 1, 1], 4),
    ([100], 100),
    ([50, 60, 70, 80, 90], 483),
    ([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 872),
    (
        [
            5,
            10,
            15,
            20,
            25,
            30,
            35,
            40,
            45,
            50,
            55,
            60,
            65,
            70,
            75,
            80,
            85,
            90,
            95,
            100,
        ],
        1912,
    ),
]


def test_exponent():
    for test_case in submit_cases:
        expected_output = test_case[1]
        result = exponent(test_case[0])
        assert round(result) == expected_output
