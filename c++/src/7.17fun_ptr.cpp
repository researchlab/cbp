// fun_ptr.cpp -- pointers to functions 

#include <iostream>
double betsy(int);
double pam(int);

// second argument is pointer to a type double function that 
// takes a type int argument 
void estimate(int lines, double (*pf)(int)); // 接收一个函数指针pf

int main() {
    using namespace std;

    int code;
    cout << "How many lines of code do you need? ";
    cin >> code;
    cout << " Here's Betsy's estimate: \n";
    estimate(code, betsy); // 函数名即函数指针
    cout << "Here's Pam's estimate: \n";
    estimate(code, pam);
    return 0;
}

double betsy(int lns)
{
    return 0.05 * lns;
}

double pam(int lns)
{
    return 0.03 * lns + 0.0005*lns * lns;
}

void estimate(int lines, double (*pf)(int))
{
    using namespace std;
    cout << lines << " lines will take ";
    cout << (*pf)(lines) << " hours\n";
}