#include<stdio.h>
#include<stdlib.h>
struct node
{
	int data;
	struct node *left;
	struct node *right;
};
struct node *tree=NULL;
struct node *insert(struct node *,int);
void preorder(struct node *);
void inorder(struct node *);
void postorder(struct node *);
int main()
{
	int option,val;
	struct node *ptr;
	do
	{
		printf("\n\n****MAIN MENU****");
		printf("\n1.Insert Element");
		printf("\n2.Preorder Traversal");
		printf("\n3.Inorder Traversal");
		printf("\n4.Postorder Traversal");
		printf("\n5.EXIT");
		printf("\nEnter your option: ");
		scanf("%d",&option);
		switch(option)
		{
			case 1:printf("\nEnter the value of new node: ");
				scanf("%d",&val);
				tree=insert(tree,val);
				printf("\nNew value inserted");
				break;
			case 2:printf("\nPreorder Traversal is: ");
				preorder(tree);
				break;
			case 3:printf("\nInorder Traversal is: ");
				inorder(tree);
				break;
			case 4:printf("\nPostorder Traversal is: ");
				postorder(tree);
				break;
		}
	}while(option!=5);
	return 0;
}
struct node *insert(struct node *tree,int val)
{
	struct node *newnode;
	if(tree==NULL)
	{
		newnode=(struct node *)malloc(sizeof(struct node *));
		newnode->data=val;
		newnode->left=NULL;
		newnode->right=NULL;
		return newnode;
	}
	if(val<tree->data)
		tree->left=insert(tree->left,val);
	if(val>tree->data)
		tree->right=insert(tree->right,val);
	return tree;
}
void preorder(struct node *tree)
{
	if(tree!=NULL)
	{
		printf("%d  ",tree->data);
		preorder(tree->left);
		preorder(tree->right);
	}
}
void inorder(struct node *tree)
{
	if(tree!=NULL)
	{
		inorder(tree->left);
		printf("%d  ",tree->data);
		inorder(tree->right);
	}
}
void postorder(struct node *tree)
{
	if(tree!=NULL)
	{
		postorder(tree->left);
		postorder(tree->right);
		printf("%d  ",tree->data);
	}
}
