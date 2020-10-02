//
//public class ArrayStack {
//
//}
import java.util.Scanner;
class stack_imp{
    int array[];
    int index=0;
    int len=0;

    public stack_imp(int n){
        this.array=new int[n];
        this.len=n;
    }
    public void insert(int v){
        if(index<len){
            array[index]=v;
            index++;
        }
        else{
            System.out.println("Stack is Full");
        }
    }
    public void delete(){
        if(index==0){
            System.out.println("Stack is Empty");
        }
        else{
            index=index-1;
        }
    }
    public void top(){
        if(index==0){
            System.out.println("Nothing on TOP");
        }
        else{   
            System.out.println(array[index-1]);
        }

    }
    public void print(){
        System.out.println("Printing the Stack---");
        for(int i=index-1;i>=0;i--){
            System.out.println(array[i]);
        }
    }


}
public class ArrayStack{
    public static void main(String[] args){
        @SuppressWarnings("resource")
		Scanner sc=new Scanner(System.in);
        System.out.println("Welcome to the Data Structure of Stack");
        System.out.println("Enter the size of array");
        int n=sc.nextInt();
        stack_imp sti=new stack_imp(n);
        while(true){
            System.out.println("Options---->");
            System.out.println("1. Push");
            System.out.println("2. Pop");
            System.out.println("3. Peek");
            System.out.println("4. Display");
            System.out.println("5. Terminate this stack");
            int choice=sc.nextInt();
            switch (choice) {
                case 1:
                    System.out.println("Enter the value to insert");
                    int a=sc.nextInt();
                    sti.insert(a);
                    sti.print();
                    break;
                case 2:
                    System.out.println("Deleting the top Element");
                    sti.delete();
                    sti.print();
                    break;
                case 3:
                    System.out.println("The top element is ->");
                    sti.top();
                    break;
                case 4:
                    System.out.println("Your Stack is");
                    sti.print();
                    break;

                default:
                	System.out.println("Invalid Choice");
            }
            if(choice==5){
                System.out.println("Thank You");
                break;
            }
        }

    }
} 