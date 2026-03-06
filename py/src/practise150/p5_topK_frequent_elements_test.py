from src.practise150.p5_topK_frequent_elements import Solution

def test_topK_frequent_elements():
    
    test_cases = [
        ([1,2,2,3,3,3] ,2, [3,2], [2,3]),
        ([7,7] ,1, [7],[7]),
        ([3, 1, 4, 4, 5, 2, 6, 1], 2 ,[4,1],[1,4]),
        ([7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9], 4, [5,11,7,10],[10,7,11,5])
    ]
    s= Solution()
    for test_case in test_cases:
        result = s.topK_frequent(test_case[0],test_case[1])
        assert result == test_case[2]
    for test_case in test_cases:
        result = s.topK_frequent2(test_case[0],test_case[1])
        assert result == test_case[3]
    for test_case in test_cases:
        result = s.topK_frequent3(test_case[0],test_case[1])
        assert sorted(result) == sorted(test_case[3])