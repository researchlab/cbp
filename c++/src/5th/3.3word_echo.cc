#include <iostream>
using std::cin; using std::cout; using std::endl;

#include <string>
using std::string;

int main()
{
    string word;
    while (cin >> word) 
        cout << word << endl; // write each word followed by a new line 
    return 0;
}