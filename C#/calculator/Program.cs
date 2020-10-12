using System;

namespace Calculator
{
    class Program
    {
        static void Main(string[] args)
        {
            int firstNum;
            int secondNum;                   //Variables for equation
            string operation;
            int answer;

            Console.WriteLine("Hello, welcome to Alex's basic calculator!");
            Console.ReadLine();

            Console.Write("Enter the first number in your basic equation: ");
            firstNum = Convert.ToInt32(Console.ReadLine());

            //User input for equation
            Console.Write("Now enter your second number in the basic equation: ");
            secondNum = Convert.ToInt32(Console.ReadLine());
            Console.Write("Ok now enter your operation ( x , / , +, -) ");
            operation = Console.ReadLine();

            if (operation == "x")
            {
                answer = firstNum * secondNum;
                Console.WriteLine(firstNum + "*" + secondNum " = " + answer);
                Console.ReadLine();
            }
            else if (operation == "/")
            {
                answer = firstNum / secondNum;
                Console.WriteLine(firstNum + " / " + secondNum + " = " + answer);
                Console.ReadLine();
            }
            //Getting answers
            else if (operation == "+")
            {
                answer = firstNum + secondNum;
                Console.WriteLine(firstNum + " + " + secondNum + " = " + answer);
                Console.ReadLine();
            }
            else if (operation == "-")
            {
                answer = firstNum - secondNum;
                Console.WriteLine(firstNum + " - " + secondNum + " = " + answer);
                Console.ReadLine();
            }
            else
            {
                Console.WriteLine("Sorry that is not correct format! Please restart!");     //Catch
                Console.ReadLine();
            }
        }
    }
}
