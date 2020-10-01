#include <stdio.h>
void swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}
void bubbleSort(int arr[], int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                swap(&arr[j], &arr[j + 1]);
            }
        }
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
    bubbleSort(num, n);
    printf("Sorted array is : \n");
    for (int i = 0; i < n; i++)
    {
        printf("%d \n", num[i]);
    }
}