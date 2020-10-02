#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <limits.h>
int row=50;
int col=5;
int A[50][5];
int loc[50];
int hashCode(int key)
    {
        return key % 47;
    }

 void insert(int value)
 {
    int index=hashCode(value);

    for(int i=0;i<row;i++)
    {
          if((A[i][0]==INT_MIN || A[i][0]==INT_MAX) && index==i)
          {
              A[i][0]=value;
              printf("%d has been inserted at pos [%d][%d] and number of probes is %d\n",value,i,0,loc[index]+1);
              loc[index]++;
          }
          else if(A[i][0]!=INT_MIN && index==i)
          {
              A[i][loc[index]]=value;
               printf("%d has been inserted at pos [%d][%d] and number of probes is %d\n",value,i,loc[index],loc[index]+1);
              loc[index]++;
          }
    }

}
void Delete_by_open_chaining(int value){
    int index=hashCode(value);
    int check=1;
    for(int i=0;i<col;i++)
    {
        if(A[index][i]== value && A[index][i]!=INT_MIN)
        {
            printf("%d  has been deleted from the position (%d)(%d)\n",value,index,i );
            check=0;
            A[index][i]=INT_MAX;
        }
    }
    if(check==1)
    {
        printf("key not found in hashmap hence can't be deleted\n");
    }

}
void search_by_open_chaining(int value)
{  int index=hashCode(value);
  int check=0;
    for(int i=0;i<col;i++){
        if(A[index][i]==value && (A[index][i]!=INT_MIN && A[index][i]!=INT_MAX))
        {
              printf("%d  has been found at the position [%d][%d]\n",value,index,i);
              check=1;
              break;
        }
    }
    if(check==0)
    {
       printf("-1\n");
    }

}



    int main(){

	for(int i=0;i<row;i++)
    {

         A[i][0]=INT_MIN; //Assigning INT_MIN indicates that cell is empty
    }
    int ch,value;
        do{
		printf("Enter your choice for open chaining \n");
		printf(" 1-> Insert\n 2-> Delete\n 3-> Searching\n \n");
		scanf("%d",&ch);
		switch(ch){
			case 1:
				 printf("Inserting element in Hashtable\n");
		     //setting up upper and lower limit for element of array
              int lower = 0, upper = 999;
               srand(time(0));
               for(int i=0;i<40;i++)
              {
                 insert((rand() % (upper - lower + 1))+lower);
              }
				break;
			case 2:
              printf("Deleting in Hashtable \n Enter the value to delete-:");
		      scanf("%d", &value);
		      Delete_by_open_chaining(value);
              break;

			case 3:
				  printf("Searching in Hashtable \n Enter the key to search-:");
		         scanf("%d", &value);
                search_by_open_chaining(value);
				break;
			default:
				printf("Enter correct choice\n");
				break;
		}
	}while(ch);
	return 0;
}

