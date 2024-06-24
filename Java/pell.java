import java.io.*;
import java.util.*;

class pell{
    
    public static void main(String args[])
    {
    Scanner sc = new Scanner(System.in);    
    //User input of the number of pell numbers
    int n = sc.nextInt();
    int a=1,b=0,c,i;
    System.out.println("First "+n+" Pell numbers are: ");
    for(i=1; i<=n; i++)
     {
      c= a + 2*b;
      System.out.print(c+" ");
      a = b;
      b = c;
     }
   }
}