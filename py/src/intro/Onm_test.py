import random

from src.intro.Onm import get_avg_brand_followers

run_cases = [
    (10, 1000, "luxa", 383.9),
    (20, 2000, "luxa", 593.25),
    (30, 3000, "luxa", 932.23),
]

submit_cases = run_cases + [
    (40, 4000, "luxa", 1495.4),
    (80, 8000, "luxa", 2608.95),
    (160, 16000, "luxa", 5920.98),
]


def test_O_nm():
    try:
        random.seed(1)
        for test_case in submit_cases:
            expected_output = test_case[3]
            all_handles = get_all_handles(test_case[0], test_case[1])
            result = round(get_avg_brand_followers(all_handles, test_case[2]), 2)
            assert result == expected_output
    except Exception as e:
        print(e)


def get_all_handles(num, audience_size):
    all_handles = []
    for i in range(num):
        m = random.randrange(
            int(audience_size - audience_size * 1.2),
            int(audience_size + audience_size * 1.2),
        )
        handles = get_user_handles(m)
        all_handles.append(handles)
    return all_handles


def get_user_handles(num):
    handles = []
    for i in range(0, num):
        m = random.randrange(0, 6)
        if m == 0:
            handles.append(f"luxaraygirl{i}")
        elif m == 1:
            handles.append(f"theprimerog{i}")
        elif m == 2:
            handles.append(f"luxafanboi{i}")
        elif m == 3:
            handles.append(f"dashlord{i}")
        elif m == 4:
            handles.append(f"saintrex{i}")
        elif m == 5:
            handles.append(f"writergurl{i}")
    return handles
