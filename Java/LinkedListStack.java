

/**
 * 
 */

/**
 * @author Varun Vaibhav Jha
 *
 */
import java.util.Scanner;
class MyStack<E> {

	StackNode<E> top;

    void push(E a) {
        StackNode<E> toAdd = new StackNode<E>(a);
        if(top==null){
            top = toAdd;
            return;
        }
        toAdd.next = top;
        top = toAdd;
    }
    E pop() {
        if(top==null)
        return null;
        if(top.next==null){
        	StackNode<E> toRemove = top;
            top = null;
            return toRemove.data;
        }
        StackNode<E> toRemove = top;
        top = top.next;
        return toRemove.data;
    }
    
    E peek() {
        if(top==null)
        return null;
        return top.data;
    }
    
	int size() {
		if (isEmpty())
			return 0;
		else {
			StackNode<E> temp = top;
			int c = 0;
			while (temp != null) {
				temp = temp.next;
				c++;
			}
			return c;
		}
	}

	boolean isEmpty() {
		return top == null;
	}

	void display() {
		if(top==null) {
			System.out.println("Empty Stack");
		}
		StackNode<E> temp = top;
		while (temp != null) {
			System.out.print(temp.data + " ");
			temp = temp.next;
		}
	}

	static class StackNode<E> {
		E data;
		StackNode<E> next;

		public StackNode(E data) {
			this.data = data;
			next = null;
		}
	}
}
public class LinkedListStack {
	public static void main(String args[]) {
		@SuppressWarnings("resource")
		Scanner in = new Scanner(System.in);
		//	Taking an Integer Stack here
		MyStack<Integer> stack = new MyStack<Integer>();
		while(true){
        	System.out.println("Options---->");
        	System.out.println("1. Push");
        	System.out.println("2. Pop");
        	System.out.println("3. Peek");
        	System.out.println("4. Display");
        	System.out.println("5. Terminate this stack");
        	int choice=in.nextInt();
        	switch (choice) {
            	case 1:
                	System.out.println("Enter the value to insert");
                	int a=in.nextInt();
                	stack.push(a);
                	stack.display();
                	break;
            	case 2:
                	System.out.println("Deleting the top Element");
                	System.out.println("Popped Element " + stack.pop());
                	stack.display();
                	break;
            	case 3:
                	System.out.println("The top element is ->");
                	stack.peek();
                	break;
            	case 4:
                	System.out.println("Your Stack is");
                	stack.display();
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

