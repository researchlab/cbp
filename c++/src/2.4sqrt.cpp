// sqrt.cpp -- using the sqrt() function 

#include <iostream>
#include <cmath> // or math.h

using namespace std;

void bucks(int num){
    cout << "$" << num << endl;
}

int main(){

    double area;
    cout << "Enter the floor area, in square feet, of your home: ";
    cin >> area;
    double side = sqrt(area);
    cout << "That's the equivalent of a square "
         << side
         << " feet to the side." << endl;
    cout << "How fascinating!" << endl;
    cout << pow(5.0, 8.0) << endl;
    cout << rand() << endl;
    bucks(10.01);
    return 0;
}

