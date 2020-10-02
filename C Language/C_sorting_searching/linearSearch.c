#include <stdio.h>

int linear_search(const int arr[], int size, int value){
  //loop to traverse through all elements of array
    for (int i = 0; i < size; ++i) {
        if (arr[i] == value)
        // if value at i^th index is equal to value then return index
            return i;
    }
    // if not found then return index size+1 which is not possible and check in main function
    return size+1;
}


int main(){
    int arr[] = {1,5,6,7,8,3,5};
    int size = sizeof(arr)/sizeof(arr[0]);
    int index = linear_search(arr, size, 3);
    if (index > size){
      printf("Element not Found");
    }
    else {
        printf("index of Element is -> %d", index);
    }
  
    return 0;
}
