 #include<iostream.h> 
#include<conio.h> 
#include<stdio.h> 
class admin { 
int admno; 
char name[30]; 
public: 
void getadmin(); 
void putadmin(); }; 
void admin::getadmin() 
{ cout<<"\nEnter admission no: "; 
cin>>admno; 
cout<<"\nEnter name: "; 
gets(name); } 
void admin::putadmin() 
{ cout<<"\nThe admission no is; "; 
cout<<admno; 
cout<<"\nThe name is: "; 
cout<<name; } 
class acadm { 
int rno; 
float marks; 
public: 
void getacadm(); 
void putacadm(); }; 
void acadm::getacadm() 
{ cout<<"\nEnter rollno: "; 
cin>>rno; 
cout<<"\nEnter marks: "; 
cin>>marks; } 
void acadm::putacadm() 
{ cout<<"\nThe rollno is: "; 
cout<<rno; 
cout<<"\nThe total marks: "; 
cout<<marks; } 
class school:public admin,public acadm //Derived class 
{ char house[15],sport[20]; 
public: 
void get_school(); 
void put_school(); }; 
void school::get_school() 
{ getadmin(); 
getacadm(); 
cout<<"\nEnter house: "; 
gets(house); 
cout<<"\nEnter sport: "; 
gets(sport); } 
void school::put_school() 
{ putadmin();
putacadm(); 
cout<<"\nYour house is: "; 
cout<<house; 
cout<<"\nYour sports is: "; 
cout<<sport; } 
void main() 
{ clrscr(); 
school obj[10]; 
int n,i,j; 
cout<<"Enter the no of students:"; 
cin>>n; 
cout<<"\nEnter student details:"; 
for(i=0;i<n;i++) 
{ obj[i].get_school(); //Input Function 
} cout<<"\nThe student details are:"; 
for(i=0;i<n;i++) 
{ obj[i].put_school(); //Output Function 
} 
getch();
}
