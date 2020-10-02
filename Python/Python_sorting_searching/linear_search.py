from typing import List

def linearSearch(arr : List, value : int):

    for i, j in enumerate(arr):
        '''
          The enumerate() method adds counter to an iterable and returns it (the enumerate object) 
          which is a tuple (i, j) i is index and j is value itself al index i
        '''

        if j == value:

            return i

    return None


if __name__ == '__main__':

    index = linearSearch([1, 4, 5, 7, 9], 5)

    print(index)
