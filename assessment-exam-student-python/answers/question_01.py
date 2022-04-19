"""
Create a function that performs an even-odd transform to a list, n times. 
Each even-odd transformation:
    - Adds 2(+2) to each odd integer.
    - Subtracts 2 (-2) to each even integer.

Example:
    even_odd_transform([3, 4, 9], 3) ➞ [9, -2, 15]
    # Since [3, 4, 9] => [5, 2, 11] => [7, 0, 13] => [9, -2, 15]

    even_odd_transform([0, 0, 0], 10) ➞ [-20, -20, -20]

    even_odd_transform([1, 2, 3], 1) ➞ [3, 0, 5]

"""

def even_odd_transform(lst,repeat):
    
    new_list = []
    
    for i in lst:
        if (i % 2) == 0:
            j = i - 2*repeat
            new_list.append(j)
        else:
            j = i + 2*repeat
            new_list.append(j)
            
    print(new_list)