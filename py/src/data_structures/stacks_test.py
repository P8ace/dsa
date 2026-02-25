from src.data_structures.stacks import Stack

def test_Stack_Size():
    submit_cases = [
        (
            [
                ("push", {"name": "Alice", "role": "Developer"}),
                ("push", {"name": "Bob", "title": "CTO"}),
                ("size", None),
            ],
            2,
            "Bob",
        ),
        (
            [
                ("push", {"name": "Charlie", "company": "TechCorp"}),
                ("push", {"name": "Diana", "skills": "Python"}),
                ("push", {"name": "Ethan", "role": "Manager"}),
                ("size", None),
            ],
            3,
            "Ethan",
        ),
        (
            [
                ("size", None),
            ],
            0,
            None,
        ),
        (
            [
                ("push", {"name": "Frank", "experience": "5 years"}),
                ("push", {"name": "Grace", "education": "MBA"}),
                ("push", {"name": "Henry", "location": "New York"}),
                ("push", {"name": "Ivy", "industry": "Finance"}),
                ("size", None),
            ],
            4,
            "Ivy",
        ),
        (
            [
                ("push", {"name": "Jack", "connections": 500}),
                ("size", None),
                ("push", {"name": "Kelly", "endorsements": 50}),
                ("size", None),
            ],
            2,
            "Kelly",
        ),
    ]
    result = None
    for test_case in submit_cases:
        stack = Stack()
        for op,value in test_case[0]:
            if op == "push":
                stack.push(value)
            elif op == "size":
                result = stack.size()

        if len(stack.items) > 0:
            name_at_top = stack.items[-1]["name"]
            assert name_at_top == test_case[2]    

            
        assert result == test_case[1]
        print(stack.items)
        
def test_peek_pop():
    run_cases = [
        (
            [
                ("push", {"name": "Alice", "role": "Developer"}),
                ("push", {"name": "Bob", "role": "Designer"}),
                ("size", None),
                ("peek", None),
                ("pop", None),
                ("size", None),
            ],
            [
                None,
                None,
                2,
                {"name": "Bob", "role": "Designer"},
                {"name": "Bob", "role": "Designer"},
                1,
            ],
        ),
        (
            [
                ("peek", None),
            ],
            [
                None,
            ],
        ),
        (
            [
                ("push", {"name": "Charlie", "company": "TechCorp"}),
                ("push", {"name": "David", "skills": ["Python", "JavaScript"]}),
                ("pop", None),
                ("pop", None),
                ("pop", None),
            ],
            [
                None,
                None,
                {"name": "David", "skills": ["Python", "JavaScript"]},
                {"name": "Charlie", "company": "TechCorp"},
                None,
            ],
        ),
    ]
    
    submit_cases = run_cases + [
        (
            [
                ("push", {"name": "Eve", "role": "Manager", "years": 5}),
                ("peek", None),
                ("push", {"name": "Frank", "role": "DevOps"}),
                ("size", None),
                ("pop", None),
                ("pop", None),
                ("pop", None),
            ],
            [
                None,
                {"name": "Eve", "role": "Manager", "years": 5},
                None,
                2,
                {"name": "Frank", "role": "DevOps"},
                {"name": "Eve", "role": "Manager", "years": 5},
                None,
            ],
        ),
    ]
    stack = Stack()
    for test_case in submit_cases:
        actual_outputs=[]
        try:
            for i, (op,value) in enumerate(test_case[0]):
                if op == "push":
                    actual_outputs.append(stack.push(value))
                elif op == "pop":
                    result= stack.pop()
                    actual_outputs.append(result)
                elif op == "peek":
                    result = stack.peek()
                    actual_outputs.append(result)
                elif op == "size":
                    result = stack.size()
                    actual_outputs.append(result)
                assert actual_outputs == test_case[1]
        except Exception as e:
            print(f"Error: {e}")
            
def test_is_balanced():
    run_cases = [
        ("(", False),
        ("()", True),
        ("(())", True),
    ]
    
    submit_cases = run_cases + [
        ("()()", True),
        ("(()))", False),
        ("((())())", True),
        ("(()(()", False),
        (")(", False),
        (")()(()", False),
        ("())(()", False),
    ]
    stack = Stack()
    for test_case in submit_cases:
        expected = test_case[1]
        result = stack.is_balanced(test_case[0])
        assert result == expected