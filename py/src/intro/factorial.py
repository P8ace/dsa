"""
for a given number find the factorial for it.
Use recursion
"""


def factorial(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return num * factorial(num - 1)
