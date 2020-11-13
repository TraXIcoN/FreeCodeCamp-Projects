#include<iostream>
#include<cmath>
using namespace std;

struct Point{
    double x;
    double y;
};
double cross_product(Point a,Point b){

    return a.x*b.y-a.y*b.x;
}
double area(Point vertices[],int n)
{
    double sum=0.0;
    for(int i=0;i<n;i++)

    {
        sum=sum+cross_product(vertices[i],vertices[(i+1)%n]);

    }
    return abs(sum)/2.0;

}
int main()
{  int n;
  double res;
   std::cout<<"enter the no of sides of ploygon";
   std::cin>>n;
   std::cout<<"enter the coordinates of vertices of plolygon";
   Point vertices[n];
   for(int i=0;i<n;i++)
   {
       std::cin>>vertices[i].x;
       std::cin>>vertices[i].y;

   }
   std::cout<<"The calculated area of the polygon is";
     res=area(vertices,n);
     std::cout<<res;
    return 0;
}
