from src.intro.geometric import geometric

TestCase = tuple[int, str, int, int]

run_cases: list[TestCase] = [
    (10, "fitness", 1, 40),
    (10, "fitness", 2, 160),
    (12, "cosmetic", 4, 972),
]

submit_cases: list[TestCase] = run_cases + [
    (15, "business", 4, 240),
    (10, "fitness", 5, 10240),
    (10, "fitness", 6, 40960),
    (10, "fitness", 7, 163840),
    (10, "fitness", 8, 655360),
    (10, "tech", 9, 5120),
]


def test_geometric():
    for test_case in submit_cases:
        expected_output = test_case[3]
        result = geometric(test_case[0], test_case[1], test_case[2])
        assert round(result) == expected_output
