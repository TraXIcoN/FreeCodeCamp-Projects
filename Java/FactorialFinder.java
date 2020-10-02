import java.util.Scanner;

class fibonacciNumber {
    public static void main(String[] args) {
        Scanner inScan = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int number = Integer.parseInt(inScan.nextLine());
        int result = 1;
        for (int i = 1; i <= number; i++) {
            result *= i;
        }
        System.out.print(result);
    }
}