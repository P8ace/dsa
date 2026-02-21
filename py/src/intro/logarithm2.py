"""
Given a list of numbers and a base
return a list of log of each item with given base.
"""

import math


def log_scale(data, base):
    result = []
    for item in data:
        result.append(math.log(item, base))
    return result
