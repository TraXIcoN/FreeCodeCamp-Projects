// Sudarshan Hiray
// 3rd October 2020
// Given an Array of Integers and rotation size, following program will rotate array by rotation size.
// It uses GCD to optimize the program and get results faster. 
// It is one of the popular coding questions in interviews.

import java.util.Scanner;

public class RotateArray {
    public static void main (String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Please enter size of the array");
        int size = scanner.nextInt();
        System.out.println("Please enter "+size+ " elements of the array");
        int[] intArray = new int[size];
        for(int i=0;i<size;i++){
            intArray[i] = scanner.nextInt();
        }

        System.out.println("\n Please enter by Rotation size");
        System.out.println("i.e. By how much you want to rotate the array");
        int rotateBy = scanner.nextInt();
        StringBuffer sb = new StringBuffer();
        for(int l=0;l<size;l++){
            sb.append(intArray[l]+" ");
        }
        System.out.println("\nOriginal Array \n");
        System.out.println(sb.toString());

        int gcd = getGCD(rotateBy, size);
        sb = new StringBuffer();
        rotateByGCD(intArray, gcd, rotateBy);

        for(int l=0;l<size;l++){
            sb.append(intArray[l]+" ");
        }
        System.out.println("\nRotated Array \n");
        System.out.println(sb.toString());

    }
    public static void rotateByGCD(int[] array, int gcd, int d){
        int temp;
        int i,j,k;
        for(i=0;i<gcd;i++) {
            temp = array[i];
            j=i;
            while(true) {
                k = j+d;
                if(k>=array.length) {
                    k = k-array.length;
                }
                if(k==i)
                    break;

                array[j] = array[k];
                j=k;
            }
            array[j]=temp;
        }
    }

    public static int getGCD(int a, int b) {
        if(b==0)
            return a;
        else
            return getGCD(b, a%b);
    }
}