/*

 * * * * * * * * * * * * * * * * * * * * * * * * *
   *           *   *           *   *           *
     *       *       *       *       *       *
       *   *           *   *           *   *
         *               *               *
       *   *           *   *           *   *
     *       *       *       *       *       *
   *           *   *           *   *           *
 * * * * * * * * * * * * * * * * * * * * * * * * *
 
 */


#include<stdio.h>

int triangle(int pattCon1, int i, int skip) 
{
 char star = '*';
 int s, j;
 for (s = pattCon1; s >= 1; s--) {
  printf("  ");
 }
 for (j = 1; j <= i; j++)
  {
 if (skip != 0) {
 if (i == 9 && j == 1) {
   continue;
 }
 }
if (i == 1 || i == 9) {
 printf("%2c", star);
}
else if (j == 1 || j == i) {
 printf("%2c", star);
 } else {
 printf("  ");
}  }
return 0;
 }


int main() {// beginning of main
int i, pattCon1 = 0, pattCon2 = -1, nbsp = -1;
for (i = 9; i >= 1; (i = i - 2)) {
  triangle(pattCon1, i, 0);
  triangle(pattCon2, i, 1);
  triangle(nbsp, i, 1);
  printf("\n");
  pattCon1++;
  pattCon2 = pattCon2 + 2;
  nbsp = nbsp + 2;
 }
 pattCon1 = 3, pattCon2 = 5, nbsp = 5;
 for (i = 3; i <= 9; (i = i + 2)) {
  triangle(pattCon1, i, 0);
  triangle(pattCon2, i, 1);
  triangle(nbsp, i, 1);
  printf("\n");
  pattCon1--;
  pattCon2 = pattCon2 - 2;
  nbsp = nbsp - 2;
 }
 return 0;
}//ending of main
