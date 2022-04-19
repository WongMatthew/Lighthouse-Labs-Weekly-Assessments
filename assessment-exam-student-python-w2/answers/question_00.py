"""
Create a function that takes a list of strings and integers, and filters out the list so that it returns a list of integers only.

Examples:
    filter_list([1, 2, 3, "a", "b", 4]) returns [1, 2, 3, 4]

    filter_list(['A', 0, 'Edabit', 1729, 'Python', '1729']) returns [0, 1729]

Notes:
    - Function always returns list
"""

def filter_list(lst):
    new_list = []
    for i in lst:
        if isinstance(i, int) == True:
            new_list.append(i)
    return new_list