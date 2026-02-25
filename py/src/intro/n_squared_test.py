from src.intro.n_squared import squared

run_cases = [
    (100, 100, "bob0 gonzalez0", True),
    (500, 500, "maria1 smith1", True),
]

submit_cases = run_cases + [
    (1000, 1000, "bob500 smith1", False),
    (2000, 2000, "bob1999 wagner1998", False),
    (3000, 3000, "sally2999 smith2998", True),
]


def test_squared():
    for test_case in submit_cases:
        expected_output = test_case[3]
        fnames = get_first_names(test_case[0])
        lnames = get_last_names(test_case[1])
        result = squared(fnames, lnames, test_case[2])
        assert result == expected_output


def get_first_names(num):
    names = []
    for i in range(num):
        m = i % 3
        if m == 0:
            names.append(f"bob{i}")
        elif m == 1:
            names.append(f"maria{i}")
        elif m == 2:
            names.append(f"sally{i}")
    return names


def get_last_names(num):
    names = []
    for i in range(num):
        m = i % 3
        if m == 0:
            names.append(f"gonzalez{i}")
        elif m == 1:
            names.append(f"smith{i}")
        elif m == 2:
            names.append(f"wagner{i}")
    return names
