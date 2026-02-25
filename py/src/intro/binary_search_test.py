from src.intro.binary_search import binary_search

run_cases = [
    (10, [i for i in range(12)], True),
    (-1, [i for i in range(20)], False),
]

submit_cases = run_cases + [
    (15, [], False),
    (0, [0], True),
    (-1, [-2, -1], True),
    (105028, [i for i in range(2000000)], True),
    (2000001, [i for i in range(2000000)], False),
]


def test_binary_search():
    for test_case in submit_cases:
        expected_output = test_case[2]
        result = binary_search(test_case[0], test_case[1])
        assert result == expected_output
