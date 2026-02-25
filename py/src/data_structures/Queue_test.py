from src.data_structures.Queue import Queue


def test_Queue():
    run_cases = [
        (
            [("push", "Rand"), ("push", "Mat"), ("peek", None), ("pop", None)],
            ["Rand", "Rand"],
        ),
        (
            [
                ("push", "Egwene"),
                ("push", "Nynaeve"),
                ("size", None),
                ("pop", None),
                ("size", None),
            ],
            [2, "Egwene", 1],
        ),
    ]

    submit_cases = run_cases + [
        ([("pop", None), ("peek", None), ("size", None)], [None, None, 0]),
        (
            [
                ("push", "Perrin"),
                ("push", "Moiraine"),
                ("push", "Lan"),
                ("pop", None),
                ("pop", None),
                ("peek", None),
            ],
            ["Perrin", "Moiraine", "Lan"],
        ),
        (
            [("push", "Thom"), ("pop", None), ("push", "Loial"), ("peek", None)],
            ["Thom", "Loial"],
        ),
    ]
    for test_case in submit_cases:
        queue = Queue()
        actual_outputs = []     
        expected = test_case[1]
        for i, (op,value) in enumerate(test_case[0]):
            print(f"Before each item in test_Case[0]: {actual_outputs}")
            if op == "push":
                queue.push(value)
            elif op == "pop":
                result = queue.pop()
                print(result)
                actual_outputs.append(result)
                print(actual_outputs)
            elif op == "peek":
                result = queue.peek()
                print(result)
                actual_outputs.append(result)
                print(actual_outputs)
            elif op == "size":
                result = queue.size()
                print(result)
                actual_outputs.append(result)
                print(actual_outputs)
            print(f"after each item in test_case[0]: {actual_outputs}")
        print("----------------------Test case ended------------------------------")
        assert actual_outputs == expected
        actual_outputs = []
        print(actual_outputs)
        
def test_matchmaking():
    run_cases = [
        [("Ted", "join"), (["Ted"], "No match found")],
        [("Barney", "join"), (["Barney", "Ted"], "No match found")],
        [("Marshall", "join"), (["Marshall", "Barney", "Ted"], "No match found")],
        [("Lily", "join"), (["Lily", "Marshall"], "Ted matched Barney!")],
        [("Robin", "join"), (["Robin", "Lily", "Marshall"], "No match found")],
        [("Carl", "join"), (["Carl", "Robin"], "Marshall matched Lily!")],
        [("Carl", "leave"), (["Robin"], "No match found")],
        [("Robin", "leave"), ([], "No match found")],
    ]
    
    submit_cases = run_cases + [
        [("Ranjit", "join"), (["Ranjit"], "No match found")],
        [("Ranjit", "leave"), ([], "No match found")],
        [("Victoria", "join"), (["Victoria"], "No match found")],
        [("Quinn", "join"), (["Quinn", "Victoria"], "No match found")],
        [("Zoey", "join"), (["Zoey", "Quinn", "Victoria"], "No match found")],
        [("Stella", "join"), (["Stella", "Zoey"], "Victoria matched Quinn!")],
    ]
    queue = Queue()
    for test_case in submit_cases:
        result = queue.matchmake(test_case[0])
        print(queue.items)
        print(result)
        assert result == test_case[1][1]
        assert queue.items == test_case[1][0]

