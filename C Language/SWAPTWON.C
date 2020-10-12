 #include<stdio.h>
 #include<conio.h>

 int main()
 {
 int a = 10, b = 20;
 printf("Before Swap a = %d and b = %d",a,b);
 a = a + b;
 b = b - a;
 a = a - b;
 printf("/nAfter Swap a = %d and b = %d",a,b);
 return 0;
 }