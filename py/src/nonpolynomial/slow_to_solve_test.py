from src.nonpolynomial.slow_to_solve import get_num_guess

def test_slow_to_solve():
    run_cases = [
        (1, 26),
        (2, 702),
        (3, 18278),
    ]
    
    submit_cases = run_cases + [
        (4, 475254),
        (5, 12356630),
        (6, 321272406),
        (7, 8353082582),
        (8, 217180147158),
        (9, 5646683826134),
    ]
    for test_case in submit_cases:
        result = get_num_guess(test_case[0])
        assert result == test_case[1]
