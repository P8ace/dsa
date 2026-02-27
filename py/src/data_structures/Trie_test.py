from src.data_structures.Trie import Trie
import json

def test_Trie():
    run_cases = [
        (
            ["dev", "devops", "devs"],
            {
                "d": {
                    "e": {
                        "v": {"*": True, "o": {"p": {"s": {"*": True}}}, "s": {"*": True}}
                    }
                }
            },
        ),
        (
            ["qa", "qaops", "qam"],
            {
                "q": {
                    "a": {"*": True, "o": {"p": {"s": {"*": True}}}, "m": {"*": True}},
                }
            },
        ),
    ]
    
    submit_cases = run_cases + [
        (
            ["pm", "po", "pojo", "pope", "cs", "ce", "ceo", "cfo"],
            {
                "p": {
                    "m": {"*": True},
                    "o": {"*": True, "j": {"o": {"*": True}}, "p": {"e": {"*": True}}},
                },
                "c": {
                    "s": {"*": True},
                    "e": {"*": True, "o": {"*": True}},
                    "f": {"o": {"*": True}},
                },
            },
        ),
    ]
    for test_case in submit_cases:
        trie = Trie()
        for word in test_case[0]:
            trie.add(word)
        assert trie.root == test_case[1]
        
def test_exists():
    run_cases = [
        (["dev", "devops", "devs", "designer"], "devops", True),
        (["manager", "qa", "dev", "intern"], "ceo", False),
        (["engineer", "developer", "janitor"], "dev", False),
    ]
    
    submit_cases = run_cases + [
        (
            ["dev", "developer", "devops", "manager"],
            "hr",
            False,
        ),
        (["qa", "qaops", "qam"], "qaops", True),
    ]

    for test_case in submit_cases:
        trie = Trie()
        for word in test_case[0]:
            trie.add(word)
        actual = trie.exists(test_case[1])
        assert actual == test_case[2]
        
def test_words_with_prefix():
    run_cases = [
        (["dev", "devops", "designer", "director"], "de", ["dev", "devops", "designer"]),
        (["manager", "intern"], "z", []),
        (["cto", "cfo", "coo", "ceo"], "c", ["cto", "cfo", "coo", "ceo"]),
    ]
    
    submit_cases = run_cases + [
        (
            ["developer", "designer", "devops", "director"],
            "de",
            ["developer", "designer", "devops"],
        ),
    ]
    
    for test_case in submit_cases:
        trie = Trie()
        for word in test_case[0]:
            trie.add(word)
        actual = trie.words_with_prefix(test_case[1])
        
        print(f"Expected: {test_case[2]}")
        print(f"Actual: {actual}")
        
        print(json.dumps(trie.root, indent=2))
        
        assert actual == sorted(test_case[2])

def test_find_matches():
    run_cases = [
        (
            ["synergy", "alignment", "leverage", "bandwidth"],
            "Let's leverage our synergy to realign our bandwidth",
            ["synergy", "leverage", "bandwidth"],
        ),
        (
            ["circle", "back", "touch", "base"],
            "Let's circle back to touch base",
            ["circle", "back", "touch", "base"],
        ),
    ]
    
    submit_cases = run_cases + [
        (
            ["pivot", "innovate", "scalable", "proactive"],
            "We need to pivot and innovate for truly scalable solutions",
            ["pivot", "innovate", "scalable"],
        ),
    ]
     
    for test_case in submit_cases:
        trie = Trie()
        for word in test_case[0]:
            trie.add(word)
        actual = trie.find_matches(test_case[1])
        print(actual)
        assert sorted(actual) == sorted(test_case[2])
        
def test_longest_common_prefix():
    run_cases = [
        (["Jerry", "Jess", "Jeremy"], "Je"),
        (["manifesto", "mantra", "management"], "man"),
    ]
    
    submit_cases = run_cases + [
        (["Cush", "Rod", "Laurel"], ""),
        (["money"], "money"),
        (["contract", "conduit", "connection"], "con"),
    ]
    for test_case in submit_cases:
        trie = Trie()
        for word in test_case[0]:
            trie.add(word)
        actual = trie.longest_common_prefix()
        assert actual == test_case[1]
    
def test_advanced_find_matches():
    run_cases = [
        (
            [
                "darnit",
                "nope",
                "bad",
            ],
            "This is a d@rn1t test with b@d words!",
            {
                "@": "a",
                "1": "i",
                "4": "a",
                "!": "i",
            },
            [
                "b@d",
                "d@rn1t",
            ],
        ),
        (
            [
                "darn",
                "shoot",
                "gosh",
            ],
            "h3ck this fudg!ng thing",
            {
                "@": "a",
                "3": "e",
            },
            [],
        ),
        (
            [
                "dang",
                "darn",
                "heck",
                "gosh",
            ],
            "d@ng it to h3ck",
            {
                "@": "a",
                "3": "e",
            },
            ["d@ng", "h3ck"],
        ),
    ]
    submit_cases = run_cases + [
        (
            [
                "darn",
                "shoot",
                "fudging",
            ],
            "sh00t, I hate this fudg!ng assignment",
            {
                "@": "a",
                "3": "e",
                "0": "o",
                "!": "i",
            },
            ["sh00t", "fudg!ng"],
        ),
    ]
    for test_case in submit_cases:
        trie = Trie()
        for word in test_case[0]:
            trie.add(word)
        actual = trie.advanced_find_matches(test_case[1], test_case[2])
        assert sorted(actual) == sorted(test_case[3])
        
if __name__ == "__main__":
    test_find_matches()