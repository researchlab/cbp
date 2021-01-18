// secref.cpp -- defining and using a reference 
#include <iostream>
int main(){
    using namespace std;
    // int rats = 101;
    // int & rodents = rats; // rodents is a reference 

    // cout << "rats = " << rats;
    // cout << ", rodents = " << rodents << endl;
    // cout << "rats address = " << &rats;
    // cout << ", rodents address = " << &rodents << endl; 

    // int bunnies = 50;
    // // 只是将bunnies 的值赋值给rodents 而不是将rodents 指向bunnies;
    // rodents = bunnies; // can we change the reference ?

    // cout << "bunnies = " << bunnies;
    // cout << ", rats = " << rats; 
    // cout << ", rodents = " << rodents << endl; 

    // cout << "bunnies address = " << &bunnies; 
    // cout << ", rodents address = " << &rodents << endl; 
    int rats = 101;
    int *pt = &rats; 
    int & rodents = *pt;
    int bunnies = 50;
    pt = &bunnies; 
    cout << " rats = " << rats << " & = " <<  &rats << endl; 
    cout << " *pt = " << *pt << " & = " << pt << endl;
    cout << " rodents = " << rodents << " & = " << &rodents << endl; 
    cout << " bunnies = " << bunnies << " & = " << &bunnies << endl;
    // output
    // rats = 101 & = 0x7ffcc82f1e1c
    // *pt = 50 & = 0x7ffcc82f1e18
    // rodents = 101 & = 0x7ffcc82f1e1c
    // bunnies = 50 & = 0x7ffcc82f1e18
    // pt 指针指向被改变, rodents 引用不会被改变; 
    
    return 0;
}