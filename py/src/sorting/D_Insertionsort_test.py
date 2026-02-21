from sorting.D_Insertionsort import insertion_sort

run_cases = [([4, 3, 2, 1], [1, 2, 3, 4]), ([9, 5, -3, 7], [-3, 5, 7, 9])]

submit_cases = run_cases + [
    ([], []),
    ([1], [1]),
    ([5, 3, 4, 1, 2], [1, 2, 3, 4, 5]),
    ([0, -2, -5, 3, 2, 1], [-5, -2, 0, 1, 2, 3]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
]


def test_insertionsort():
    for test_case in submit_cases:
        expected_output = test_case[1]
        result = insertion_sort(test_case[0])
        assert result == expected_output
