from src.nonpolynomial.subset_sum import subset_sum

def test_subset_sum():
    run_cases = [
        ([3, 34, 4, 12, 5, 2], 9, True),
        ([1, 2, 3], 7, False),
    ]
    
    submit_cases = run_cases + [
        ([1, 2, 3, 8, 9, 10], 7, False),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 15, True),
        ([3, 2, 7, 1], 6, True),
        ([10, 20, 30, 40, 50], 60, True),
        (
            [1, 2, 3, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
            500,
            False,
        ),
    ]
    
    for test_case in submit_cases:
        result = subset_sum(test_case[0], test_case[1])
        assert result == test_case[2]