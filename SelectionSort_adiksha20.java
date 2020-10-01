import java.util.*;
class SelectionSort
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();// Enter the size of array
        int a[]=new int[n]; //Initializing and declaring an array
        for(int i=0;i<n;i++)
        {
            a[i]=sc.nextInt();   // Input the values of array
        }
        
       
        // One by one find the minimum element from the ith element to the end of an array
        for(int i=0;i<n;i++)
        {
            //Find the minimum element in unsorted array
            int minindex=i;         
            for(int j=i;j<n;j++)
            {
                if(a[j]<a[minindex])
                {
                    minindex=j;
                }
            }
            
            //Swap the found element with the ith element
            int temp=a[minindex];
            a[minindex]=a[i];
            a[i]=temp;
            
        }
        
        // Print the sorted array
        for(int i=0;i<n;i++)
        {
            System.out.print(a[i]+" ");
        }
    }
}