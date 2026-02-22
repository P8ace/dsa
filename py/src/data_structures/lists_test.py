from data_structures.lists import count_marketers, last_work_experience

def test_count_marketers():
    run_cases = [
        (["developer", "marketer", "designer"], 1),
        (["marketer", "marketer", "developer", "marketer"], 3),
    ]
    
    submit_cases = run_cases + [
        ([], 0),
        (["developer", "designer", "product manager"], 0),
        (["marketer"], 1),
        (["MARKETER", "Marketer", "marketer"], 3),
    ]
    for test_case in submit_cases:
        expected = test_case[1]
        result = count_marketers(test_case[0])
        assert result == expected

def test_last_work_experience():
    run_cases = [
        (["Software Engineer", "Data Analyst", "Project Manager"], "Project Manager"),
        (["Intern", "Junior Developer"], "Junior Developer"),
    ]
    
    submit_cases = run_cases + [
        ([], None),
        (["CEO"], "CEO"),
        (["Cashier", "Supervisor", "Manager", "Director"], "Director"),
    ]
    for test_case in submit_cases:
        expected = test_case[1]
        result = last_work_experience(test_case[0])
        assert result == expected
