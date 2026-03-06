from src.practise150.P6_encode_decode_string import Solution

def test_encode_decode_string():
    test_cases=[
            ["Hello","World"],
             ["abc","!@"]
    ]
    s = Solution()      
    for test_case in test_cases:
        result = s.encode(test_case)
        assert result != test_case
        result2 = s.decode(result)
        assert result2 == test_case