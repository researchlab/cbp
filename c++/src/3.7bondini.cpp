// bondini.cpp -- using escape sequences 
#include <iostream>
using namespace std;

int main(){
    cout << "\aOperation \"HyperHyper\" is now activated!\n";
    cout << "Enter your agent code:___\b\b\b";
    long code;
    cin >> code;
    cout << "\aYou entered " << code << " ...\n";
    cout << "\aCode verified! Proceed width Plan Z3!\n";
    bool start = -100 , stop = 0;
    cout << bool(start) << stop << endl;
    return 0;
}