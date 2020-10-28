"""
Given two sets
Find symmetric diffrence of these two sets.

Example:
s1 = {1, 2 ,3}
s2 = {2, 3, 4}
symmetric diffrence: s1^s2 = {1, 4}
"""

def symmetricDifference(set1, set2):
    """
    Input: {1, 2, 3}
           {2, 3, 4}
    Output: {1, 4}
    """

    # using set1 ^ set2
    set3 = set1^set2
    print(set3)

    # using symmetric_difference
    set4 = set1.symmetric_difference(set2)
    print(set4)

set1 = {1, 2, 3}
set2 = {2, 3, 4}
symmetricDifference(set1, set2)
