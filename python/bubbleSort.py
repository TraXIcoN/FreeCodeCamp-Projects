# Bubble Sort in Python
  
from typing import List

def bubbleSort(arr : List) -> List: 
    n = len(arr) 
  
    sortedList = arr.copy()
    # loop to traverse through all elements of list
    for i in range(n): 
  
        # Last i elements have already been sorted
        for j in range(0, n-i-1): 
            
            # if elemrnt is found greater then swap those
            if sortedList[j] > sortedList[j+1] : 
                sortedList[j], sortedList[j+1] = sortedList[j+1], sortedList[j] 

    return sortedList


if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90] 
    
    sortedArray = bubbleSort(arr)
    print(sortedArray)
