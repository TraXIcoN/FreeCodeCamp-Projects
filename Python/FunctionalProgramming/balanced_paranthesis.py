''' A recursive algorithm for producing all permutations of a balanced parentheses 
    which makes full use of pure functional programming.
'''

from typing import List
from pprint import pprint

def main() -> None:
    ''' Main runner script for user interaction and evaluation '''
    n = int(input("Enter a non-negative integer: "))
    while n < 0:
        n = int(input(f"{n} < 0. Please input a non-negative integer: "))
        pass

    results = balanced_parentheses(n)
    
    print(f"Possible combinations of {n} balanced parentheses:")
    pprint(results)

def balanced_parentheses(n: int) -> List[str]:
    ''' Construct all combinations of n balanced parentheses.

        Arguments
        ---------
        n : int
            the number of allowed balanced parentheses
    '''
    return __make_balenced_parentheses(n, n)

def __make_balenced_parentheses(n_open: int, n_close: int, buf: str = '') -> List[str]:
    ''' Helper function that is called recursively to construct 
        the balanced parentheses combinations.
    '''
    # Have all parentheses been opened and closed?
    if n_open == 0 and n_close == 0:
        return [buf]
    
    left = []
    # Can more open parentheses can be made?
    if n_open > 0:
       left = __make_balenced_parentheses(n_open-1, n_close, f'{buf}(')
    
    right = []
    # Can any parentheses be closed?
    if n_close > n_open:
        right = __make_balenced_parentheses(n_open, n_close-1, f'{buf})')
    
    return left + right

if __name__ == "__main__":
    main()

