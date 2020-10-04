//Umang Agarwal
//5th October 2020
//This program checks if a number is prime or not. A prime number is a number which is only divisble by 1 and itself
import java.util.*;
public class prime
{
	public static void main(String args[])
	{
		Scanner sc = new Scanner (System.in);
		System.out.println("Enter number to be checked");
		int num = sc.nextInt();//Stores user input
		if(num==0||num==1)
    {
        System.out.println("The number entered is not Prime");
        return;
    }
    for (int i = 2;i<=(int)Math.sqrt(num);i++)
		{
			if(num%i==0)
			{
				System.out.println("The number entered is not Prime");
        return;
        //if any number between 2 and square root of the number is a factor print not prime and exit
			}
		}
		System.out.println("The number entered is Prime");//if execution reaches this statement, number is prime
	}
}
