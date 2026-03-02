from src.nonpolynomial.prime_factorization import prime_factors

def test_prime_factors():
    run_cases = [(8, [2, 2, 2]), (10, [2, 5]), (24, [2, 2, 2, 3]), (13, [13])]
    
    submit_cases = run_cases + [
        (49, [7, 7]),
        (77, [7, 11]),
        (4, [2, 2]),
        (64, [2, 2, 2, 2, 2, 2]),
        (63, [3, 3, 7]),
        (36, [2, 2, 3, 3]),
    ]
    
    for test_case in submit_cases:
        result = prime_factors(test_case[0])
        assert result == test_case[1]