from src.practise150.p15_best_stock_to_sell_and_buy import Solution

def test_max_profit():
    test_cases = [
        ([10,1,5,6,7,1], 6),
        ([10, 8, 7, 5, 2], 0)
    ]
    
    s = Solution()
    
    for test_case in test_cases:
        assert test_case[1] == s.max_profit(test_case[0])
        assert test_case[1] == s.max_profit2(test_case[0])