import time

from src.sorting.E_Quicksort import quick_sort

# from E_Quicksort import quick_sort

run_cases = [
    ([2, 1, 3], 0, 2, [1, 2, 3]),
    ([9, 6, 2, 1, 8, 7], 0, 5, [1, 2, 6, 7, 8, 9]),
]

submit_cases = run_cases + [
    ([], 0, -1, []),
    ([1], 0, 0, [1]),
    ([1, 2, 3, 4, 5], 0, 4, [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], 0, 4, [1, 2, 3, 4, 5]),
    ([0, 1, 6, 5, 7, 3, 2, 8, 5, -9], 0, 9, [-9, 0, 1, 2, 3, 5, 5, 6, 7, 8]),
    ([0, 1, 6, 4, 7, 3, 2, 8, 5, -9], 0, 9, [-9, 0, 1, 2, 3, 4, 5, 6, 7, 8]),
]


def test_quicksort():
    for test_case in submit_cases:
        expected_output = test_case[3]
        start = time.time()
        result = quick_sort(test_case[0], test_case[1], test_case[2])
        end = time.time()
        timeout = 1.00
        if (end - start) < timeout:
            assert result == expected_output


if __name__ == "__main__":
    test_quicksort()
