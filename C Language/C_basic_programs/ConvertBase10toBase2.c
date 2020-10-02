#include <stdio.h>
#include <stdlib.h>
 
int main()
{ //beginning of main
    int num,rem;// variables
 
    printf("BASE 10 TO BASE 2 CONVERTER\n\n");
    printf("Enter the base 10 number that you want to convert:");// input
    scanf("%d", &num);
 
    while(num!=0)
    {
        rem=num%2;
        num=num/2;
        printf("%d", rem);//printing result
    }
    return 0;
}//end of main
