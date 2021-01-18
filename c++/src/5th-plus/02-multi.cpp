#include <iostream>

using namespace std;

int main(int argc, char const *argv[]){
    cout << "input a number:"<<endl;
    int v1 = 0;
    cin >> v1;

    for (int i =1; i <= v1; i++){
        for(int j = 1; j <= i; j++){
            cout << j << "*" << i << "=" << j*i <<" ";
        }
        clog << "clog";
        cout << endl;
    }
}