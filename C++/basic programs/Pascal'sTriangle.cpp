//Pascal triangle in C++

#include <iostream>
using namespace std;

int main()
{
    int no_rows, c = 1;

    cout << "Enter the number of rows: ";
    cin >> no_rows;

    for(int i = 0; i < no_rows; i++)
    {
        for(int blk = 1; blk <= no_rows-i; blk++)
            cout <<"  "; //printing space to show triangular form

        for(int j = 0; j <= i; j++)
        {
            if (j == 0 || i == 0)
                c = 1;  
            else
                c = c*(i-j+1)/j;

            cout << c << "   ";  //printing numbers to form the triangle 
        }
        cout << endl;
    }

    return 0;
}
