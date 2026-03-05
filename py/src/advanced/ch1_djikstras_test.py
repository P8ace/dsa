from src.advanced.ch1_djikstras import get_path, next_nearest_node, dijkstra

def test_get_path():
    TestCase = tuple[str, dict[str, str], list[str]]
    run_cases: list[TestCase] = [
        (
            "Minas Tirith",
            {"Minas Tirith": "Isengard", "Isengard": "Gondor", "Gondor": "Rivendell"},
            ["Rivendell", "Gondor", "Isengard", "Minas Tirith"],
        ),
        (
            "Minas Tirith",
            {"Minas Tirith": "Rivendell", "Isengard": "Gondor", "Rivendell": "Isengard"},
            ["Gondor", "Isengard", "Rivendell", "Minas Tirith"],
        ),
    ]
    
    submit_cases: list[TestCase] = run_cases + [
        ("Minas Tirith", {}, ["Minas Tirith"]),
        ("Rivendell", {"Minas Tirith": "Rivendell"}, ["Rivendell"]),
        (
            "Gondor",
            {
                "Minas Tirith": "Isengard",
                "Isengard": "Gondor",
                "Gondor": "Rivendell",
                "Bree": "Minas Tirith",
            },
            ["Rivendell", "Gondor"],
        ),
    ]
    
    for test_case in submit_cases:
        result = get_path(test_case[0], test_case[1])
        
        assert result == test_case[2]
        
def test_next_nearest_node():
    run_cases = [
        (
            {"Minas Tirith": 4, "Isengard": 2, "Gondor": 3, "Mirkwood": 1},
            {"Minas Tirith", "Gondor"},
            "Gondor",
        ),
        (
            {"Minas Tirith": 1, "Isengard": 2, "Gondor": 2, "Mirkwood": 1},
            {"Minas Tirith", "Gondor"},
            "Minas Tirith",
        ),
    ]
    
    submit_cases = run_cases + [
        ({}, set(), None),
        (
            {"Minas Tirith": 1, "Isengard": 2, "Gondor": 2, "Mirkwood": 1},
            {"Isengard", "Mirkwood"},
            "Mirkwood",
        ),
        (
            {
                "Minas Tirith": 3,
                "Isengard": 8,
                "Gondor": 7,
                "Mirkwood": 12,
                "Rivendell": 10,
            },
            {"Isengard", "Mirkwood"},
            "Isengard",
        ),
    ]
    
    for test_case in submit_cases:
        result = next_nearest_node(test_case[0], test_case[1])
        
        assert result == test_case[2]
        
def test_djikstras():
    run_cases = [
        (
            {
                "Minas Tirith": {"Isengard": 4, "Gondor": 1},
                "Isengard": {"Minas Tirith": 4, "Bree": 3, "Mirkwood": 8},
                "Gondor": {"Minas Tirith": 1, "Bree": 2, "Misty Mountains": 6},
                "Bree": {"Gondor": 2, "Isengard": 3, "Mirkwood": 4},
                "Mirkwood": {"Bree": 4, "Isengard": 8, "Lothlorien": 2},
                "Misty Mountains": {"Gondor": 6, "Lothlorien": 8},
                "Lothlorien": {"Misty Mountains": 8, "Mirkwood": 2},
            },
            "Minas Tirith",
            "Lothlorien",
            ["Minas Tirith", "Gondor", "Bree", "Mirkwood", "Lothlorien"],
        ),
        (
            {
                "Minas Tirith": {"Isengard": 4, "Gondor": 1},
                "Isengard": {"Minas Tirith": 4, "Bree": 3, "Mirkwood": 8},
                "Gondor": {"Minas Tirith": 1, "Bree": 2, "Misty Mountains": 6},
                "Bree": {"Gondor": 2, "Isengard": 3, "Mirkwood": 4},
                "Mirkwood": {"Bree": 4, "Isengard": 8, "Lothlorien": 2},
                "Misty Mountains": {"Gondor": 6, "Lothlorien": 8},
                "Lothlorien": {"Misty Mountains": 8, "Mirkwood": 2},
            },
            "Isengard",
            "Gondor",
            ["Isengard", "Bree", "Gondor"],
        ),
    ]
    
    submit_cases = run_cases + [
        (
            {"Minas Tirith": {"Isengard": 2}, "Isengard": {"Minas Tirith": 2}},
            "Minas Tirith",
            "Isengard",
            ["Minas Tirith", "Isengard"],
        ),
        (
            {
                "Erebor": {"Minas Tirith": 2, "Isengard": 1},
                "Minas Tirith": {"Erebor": 3, "Isengard": 4, "Gondor": 8},
                "Isengard": {"Erebor": 4, "Minas Tirith": 2, "Bree": 2},
                "Gondor": {"Minas Tirith": 2, "Bree": 7, "Osgiliath": 4},
                "Bree": {"Isengard": 1, "Gondor": 11, "Osgiliath": 5},
                "Osgiliath": {"Gondor": 3, "Bree": 5},
            },
            "Erebor",
            "Osgiliath",
            ["Erebor", "Isengard", "Bree", "Osgiliath"],
        ),
        (
            {
                "Erebor": {"Minas Tirith": 2, "Isengard": 1},
                "Minas Tirith": {"Erebor": 3, "Isengard": 4, "Gondor": 8},
                "Isengard": {"Erebor": 4, "Minas Tirith": 2, "Bree": 2},
                "Gondor": {"Minas Tirith": 2, "Bree": 7, "Osgiliath": 4},
                "Bree": {"Isengard": 1, "Gondor": 11, "Osgiliath": 5},
                "Osgiliath": {"Gondor": 3, "Bree": 5},
            },
            "Minas Tirith",
            "Bree",
            ["Minas Tirith", "Isengard", "Bree"],
        ),
    ]
    
    for test_case in submit_cases:
        result = dijkstra(test_case[0], test_case[1], test_case[2])
        
        assert result == test_case[3]