#include <stdio.h>
void insertionSort(int arr[], int n)
{
    int i, hole, j;
    for (i = 1; i < n; i++)
    {
        hole = arr[i];
        j = i - 1;
        while (j >= 0 && arr[j] > hole)
        {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = hole;
    }
}
void main()
{
    int n;
    printf("Enter the size of the array: ");
    scanf("%d", &n);
    int num[n];
    printf("Enter the numbers :");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &num[i]);
    }
    printf("Intial array is : \n");
    for (int i = 0; i < n; i++)
    {
        printf("%d \n", num[i]);
    }
    insertionSort(num, n);
    printf("Sorted array is : \n");
    for (int i = 0; i < n; i++)
    {
        printf("%d \n", num[i]);
    }
}