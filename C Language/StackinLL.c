#include <stdio.h>  
#include <stdlib.h>  
void push();  
void pop();  
void display(); 
void pick(); 
void reverseList();
struct node   
{  
int val;  
struct node *next;  
};  
struct node *top;  
  
void main ()  
{  
    int choice=0;     
    printf("\n Stack \n");  
    printf("\n  \n");  
    while(choice != 4)  
    {  
        printf("\n\nChose one from the below options...\n");  
        printf("\n1.Push\n2.Pop\n3.Show\n4.Peep\n5.Reverse\n6.Exit");  
        printf("\n Enter your choice \n");        
        scanf("%d",&choice);  
        switch(choice)  
        {  
            case 1:  
            
            {   
                push();  
                break;  
            }  
            case 2:  
            {  
                pop();  
                break;  
            }  
            case 3:  
            {  
                display();  
                break;  
            }  
            case 4:
            	{
            		pick();
            		break;
				}
			case 5:
				{
					 
    				printf("\nReversed Linked list \n"); 
    				reverseList();
				}
            case 6:   
            {  
                printf("Exiting...."); 
				exit(0) ;
                break;   
            }  
            default:  
            {  
                printf("Please Enter valid choice ");  
            }   
    };  
}  
}  
void push ()  
{  
    int val;  
    struct node *ptr = (struct node*)malloc(sizeof(struct node));   
    if(ptr == NULL)  
    {  
        printf("not able to push the element");   
    }  
    else   
    {  
        printf("Enter the value\n");  
        scanf("%d",&val);  
        if(top==NULL)  
        {         
            ptr->val = val;  
            ptr -> next = NULL;  
            top=ptr;  
        }   
        else   
        {  
            ptr->val = val;  
            ptr->next = top;  
            top=ptr;  
               
        }  
        printf("Item pushed");  
          
    }  
}  
  
void pop()  
{  
    int item;  
    struct node *ptr;  
    if (top == NULL)  
    {  
        printf("Underflow");  
    }  
    else  
    {  
        item = top->val;  
        ptr = top;  
        top = top->next;  
        free(ptr);  
        printf("Item popped");  
          
    }  
}  
void display()  
{  
    int i;  
    struct node *ptr;  
    ptr=top;  
    if(ptr == NULL)  
    {  
        printf("Stack is empty\n");  
    }  
    else  
    {  
        printf("Printing Stack elements \n");  
        while(ptr!=NULL)  
        {  
            printf("%d\n",ptr->val);  
            ptr = ptr->next;  
        }  
    }  
}
void pick()
{
	printf("%d ",top->val);
} 
 
void reverseList()
{
    struct node *prevNode, *curNode;

    if(top != NULL)
    {
        prevNode = top;
        curNode = top->next;
        top = top->next;

        prevNode->next = NULL; // Make first node as last node

        while(top != NULL)
        {
            top = top->next;
            curNode->next = prevNode;

            prevNode = curNode;
            curNode = top
			;
        }

        top = prevNode; // Make last node as head

        printf("SUCCESSFULLY REVERSED LIST\n");
    }
}
