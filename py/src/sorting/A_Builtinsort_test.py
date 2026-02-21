from sorting.A_Builtinsort import Influencer, vanity_sort

theprimeagen = Influencer(100, 1)
pokimane = Influencer(800, 2)
spambot = Influencer(0, 200)
lane = Influencer(10, 2)
badcop = Influencer(1, 2)

run_cases = [
    ([badcop, lane], [badcop, lane]),
    ([lane, badcop, pokimane], [badcop, lane, pokimane]),
    ([spambot, theprimeagen], [theprimeagen, spambot]),
]

submit_cases = run_cases + [
    ([], []),
    ([lane], [lane]),
    (
        [pokimane, theprimeagen, spambot, badcop, lane],
        [badcop, lane, theprimeagen, pokimane, spambot],
    ),
]


def test_A_sorting():
    for test_case in submit_cases:
        expected_output = test_case[1]
        result = vanity_sort(test_case[0])
        assert result == expected_output
