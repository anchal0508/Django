#include <iostream>
using namespace std;
int main()
{
    cout << "Hello";

    for (int j = 0; j < 10; j++)
    {
        for (int i = 0; i < 10; i++)
        {
            if ((j > 2 && j < 8 && i>2 && i<8) || (i==9 && j==0))
            {
                cout << ' ' << ' ';
            }
            else
                cout << '*' << ' ';
        }
        cout << endl;
    }
}