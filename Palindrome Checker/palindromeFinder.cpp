#include <iostream>
#include <cstring>
using namespace std;

int main() {
    char pal[10]; bool isPal;
    cout<<"Enter Any String : ";
    cin>>pal;
    cout<<strlen(pal);
    for(int i=0, j=strlen(pal)-1; i<strlen(pal)/2; i++,j--)
    {
        if(pal[i]!=pal[j]){ isPal = false; break; }
        else isPal=true;
    }
    if(isPal==true) cout<<"String is Pallindrome";
    else cout<<"String is not Pallindrome";
	return 0;
}