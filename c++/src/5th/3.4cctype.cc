#include <string>
using std::string;

#include <cctype>
using std::isupper; using std::toupper;
using std::islower; using std::tolower; 
using std::isalpha; using std::isspace;

#include <iostream>
using std::cout; using std::endl;

int main()
{
    // string 初始化方法之一
    string s("Hello world!!");
    // punct_cnt has the same type that s.size returns 
    // decltype 选择并返回操作数的数据类型
    decltype(s.size()) punct_cnt = 0;

    // count the number of punctuation characters in s 
    for (auto c : s )   // for every char in s 
        if (ispunct(c)) // if the character is punctuation 
            ++punct_cnt; // increment the punctuation counter 

    cout << punct_cnt 
         << " punctuation characters in "<< s << endl; 
    
    int tmp[] = {1,2,3};
    // for 循环方式  全部循环
    for (int i : tmp )
            cout << i << endl;
    
    // convert s to uppercase 
    string orig = s;
    for (auto &c : s ) // for every char in s (note: c is a reference)
        c = toupper(c);
    cout << s << endl;

    // convert first word in s to uppercase 
    s = orig; // restore s to original case 
    decltype(s.size()) index = 0;

    // process characters in s until we run out of characters or we hit a whitespace 
    while(index != s.size() && !isspace(s[index])){
        // s[index] returns a reference so we can change 
        // the underlying character
        s[index] = toupper(s[index]);
        // increment the index to look at the next character
        // on the next iteration
        ++index;
    }

    cout << s << endl; 

    return 0;
}