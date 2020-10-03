//Standard selection sort algorithm
void Selection_sort(int arr[], int n){
    int min_index;
    for(int i = 0 ; i < n - 1 ; i++ ){
        min_index=i;
        for ( int j = i+1 ; j < n; j ++){
            if(arr[j] <  arr [min_index]){
                min_index=j;
            }
        }
        swap(arr[min_index], arr[i]);
    }
}
// Function to swap the values of the array, part of bubble sort
void swap(int *a, int *b){
    int temp;
    temp=*a;
    *a=*b;
    *b=temp;
}
//Function to print the array after sorting
void printArray(int arr[],int n){
    for( int i = 0; i < n; i ++){
        cout<<arr[i]<<" ";
    } 
}
