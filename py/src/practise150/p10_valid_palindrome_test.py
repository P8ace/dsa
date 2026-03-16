from src.practise150.p10_valid_palindrome import Solution

def test_valid_palindrome():
    test_cases=[
        ("Was it a car or a cat I saw?", True),
        ("tab a cat", False)
    ]
    
    s= Solution()
    for test_case in test_cases:
        result = s.valid_palindrome(test_case[0])
        assert result == test_case[1]