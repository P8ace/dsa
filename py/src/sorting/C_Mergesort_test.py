from sorting.C_Mergesort import merge_sort

submit_cases =[
    ([3, 2, 1], [1, 2, 3]), 
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([], []),
    ([7], [7]),
    ([4, -7, 1, 0, 5], [-7, 0, 1, 4, 5]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
]

def test_merge_sort():
    for test_case in submit_cases:
        expected_output = test_case[1]
        result = merge_sort(test_case[0])
        assert result == expected_output