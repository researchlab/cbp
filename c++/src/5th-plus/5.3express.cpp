// express.cpp -- values of expressions 
#include <iostream>
using namespace std;
int main() {
    int x;
    cout << "The expression x = 100 has the value";
    cout << (x = 100) << endl;
    cout << "Now x = " << x << endl; 
    cout << "The expression x < 3 has the value ";
    cout << (x < 3 ) << endl;
    cout << "The expression x > 3 has the value ";
    cout << (x > 3 ) << endl;
    cout.setf(ios_base:: boolalpha); // a newer c++ feature 
    // cout 在显示bool 值之前将它们转换为int, 但cout.setf(ios_base::boolalpha) 函数调用
    // 设置了一个标记, 该标记命令cout 显示true 和false,而不是0 和1;
    cout << "The expression x < 3 has the value ";
    cout << (x < 3 ) << endl;
    cout << "The expression x > 3 has the value ";
    cout << (x > 3 ) << endl;
    return 0;
}