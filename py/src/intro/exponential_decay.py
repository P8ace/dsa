"""
Given a factor lost per day, find the value of a initial number for number of days

result = initial number * ( (1 - factor lost daily) ^ no.of days)
"""


def exponential_decay(num, factor, days):
    return num * ((1 - factor) ** days)
