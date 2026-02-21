"""
nested loop : O(n^2)
"""


def squared(first_names, last_names, full_name):
    for first_name in first_names:
        for last_name in last_names:
            if first_name + " " + last_name == full_name:
                return True
    return False
