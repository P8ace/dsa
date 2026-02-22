from t_polynomial_algorithms.Order_Kn import letter_combinations

run_cases = [
    ("", 0, [], ""),
    ("67", 12, ["mp", "mq", "mr"], "op"),
    ("43556", 243, ["gdjjm", "gdjjn", "gdjjo"], "hello"),
    ("2668338", 2187, ["ammtddt", "ammtddu", "ammtddv"], "bootdev"),
]

submit_cases = run_cases + [
    ("420", 0, [], "ValueError"),
    ("7878326", 3888, ["ptptdam", "ptptdan", "ptptdao"], "rustfan"),
    ("4568346", 2187, ["gjmtdgm", "gjmtdgn", "gjmtdgo"], "ilovego"),
]


def test_combinations():
    for test_case in submit_cases:
        try:
            result = letter_combinations(test_case[0])
            actual_length = len(result)
            if test_case[1] == 0 and actual_length == test_case[1]:
                # assert True
                continue
            actual_initial = result[:3]
            actual_contains = test_case[3] in result


            assert actual_length == test_case[1]
            assert actual_initial == test_case[2]
            assert actual_contains
        except ValueError as ve:
            print(ve)
            if test_case[1] == 0 and test_case[3] == "ValueError":
                assert True
