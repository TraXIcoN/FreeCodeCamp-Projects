#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<malloc.h>

struct node
{
    int data;
    struct node *next;
};

struct node *start=NULL;
struct node *create_ll(struct node *);
struct node *display(struct node *);

int main(void)
{
    int option;
    do
    {
        printf("\n Enter 1 for create");
        printf("\n Enter 2 for display");
        printf("\n Enter 3 for exit");
        printf("\n Enter option:");
        scanf("%d",&option);
        switch(option)
        {
        case 1:
            start = create_ll(start);
            break;
        case 2:
            start = display(start);
            break;
        }
    }
    while(option!=13);
return 0;
}

struct node *create_ll(struct node *start)
{
    struct node *new_node,*ptr;
    int num;
    printf("\n Enter -1 to exit");
    printf("\n Enter data:");
    scanf("%d",&num);
    while(num!=-1)
    {
        new_node=(struct node *)malloc(sizeof(struct node));
        new_node->data=num;
        if(start==NULL)
        {
            new_node->next=NULL;
            start=new_node;
        }
        else
        {
            ptr=start;
            while(ptr->next!=NULL)
            {
                ptr=ptr->next;
            }
            ptr->next=new_node;
            new_node->next=NULL;
        }
        printf("\n Enter data:");
        scanf("%d",&num);
    }
    return start;
}

/*struct node *display(struct node *start)
{
    struct node *ptr;
    ptr=start;
    while(ptr->next!=NULL);
    {
    printf("\t %d",ptr->data);
    ptr=ptr->next;
    }
    return start;
}*/
struct node *display(struct node *start)
{
	struct node *ptr;
	ptr = start;
	while(ptr != NULL)
	{
		printf("\t %d",ptr -> data);
		ptr = ptr -> next;
	}
	return start;
}
