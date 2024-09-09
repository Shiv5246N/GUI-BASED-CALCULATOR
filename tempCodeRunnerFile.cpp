#include<iostream>
using namespace std;
class Calculate
{
    public:
    void cube(int a)
    {
        cout<<"Cube of integer = "<<a*a*a<<endl;
    }
    void cube(float b)
    {
     cout<<"Cube of float = "<<b*b*b<<endl;   
    }
};
int main()
{
    Calculate c1;
    c1.cube(5);
    c1.cube(5.5);
    return 0;
}