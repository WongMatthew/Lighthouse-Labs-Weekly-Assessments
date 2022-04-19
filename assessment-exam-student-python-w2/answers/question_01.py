"""
Create a function that returns the mean of all digits.

Example:
    mean(42) ➞ 3.0

    mean(12345) ➞ 3.0

    mean(666) ➞ 6.0

Notes:
    - Function should always return float
"""


def mean(digits):
    counter = 0
    total = 0
    for i in str(digits):
        counter += 1
        total += int(i)
    return total / counter