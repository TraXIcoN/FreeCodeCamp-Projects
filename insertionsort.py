from typing import List

def insertionSort(arr : List) -> List: 

    sortedList = arr.copy()

      for i in range(1, len(arr)): 
  
        key = sortedList[i]
        j = i-1
        while j >=0 and key < sortedList[j] : 
                sortedList[j+1] = sortedList[j] 
                j -= 1
        sortedList[j+1] = key 


    return sortedList


if __name__ == '__main__':

    arr = [64, 34, 25, 12, 22, 11, 90] 

    sortedArray = insertionSort(arr)
    print(sortedArray)
  
  
