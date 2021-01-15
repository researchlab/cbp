// instr1.cpp -- reading more than one string 
#include <iostream>

int main(){
    using namespace std;
    const int ArSize = 20;
    char name[ArSize];
    char dessert[ArSize];

    cout << "Enter your name: \n";
    cin >> name;
    // cin.getline(name,ArSize); // reads through newline;
    cout << "Enter your favorite dessert: \n";
    cin >> dessert;
    // cin.getline(dessert, ArSize);
    // cin.get(name, ArSize); // read first line
    // cin.get(); // read newline
    // cin.get(dessert, ArSize); // read second line
    // cin.get(name,ArSize).get();
    cout << "I have some delicious " << dessert;
    cout << " for you. " << name << ".\n";
    return 0;
}